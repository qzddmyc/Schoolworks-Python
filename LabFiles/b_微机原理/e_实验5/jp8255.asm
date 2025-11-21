	.MODEL	TINY		
PA_8255		EQU	0270H           
PB_8255		EQU	0271H
PC_8255		EQU	0272H
CTRL_8255	EQU	0273H
	.STACK	100
	.DATA    
buffer          DB      ?               
SEG_TAB		DB	0C0H, 0F9H,0A4H,0B0H, 99H, 92H, 82H,0F8H    
		DB	080H, 90H, 88H, 83H,  0C6H,0A1H,86H,8EH,0FFH 

	.CODE
START:  	MOV     AX,@DATA
        	MOV     DS,AX
        	MOV	ES,AX
        	NOP		
		MOV	DX,CTRL_8255	;8255初始化
		MOV	AL,89H
		OUT	DX,AL		
        	LEA	SI,buffer
		MOV	AL,10H          ;默认数码管不显示
		MOV     [SI],AL
		
		CALL	DIR             ;调用显示子程序

MAIN2:		LEA	DI,buffer       
		CALL	Getkey          ;得到按键在SEG_TAB中的值放入AL
		STOSB                   ;将AL赋值给DI指向的地址
		CALL	DIR            		
		JMP	MAIN2

DIR		PROC	NEAR            
		PUSH	AX
		PUSH	BX
		PUSH	DX
		LEA	SI,buffer	;置显示缓冲器初值	
		MOV	AL,[SI]
		LEA	BX,SEG_TAB				
		XLAT			;查表取显示数据->AL			
		MOV	DX,PA_8255
		OUT	DX,AL		;AL段数据->8255 PA口		
		MOV     DX,PB_8255
		MOV     AL,0		;位码控制GND端低电平有效, 显示8位数据管
		OUT     DX,AL           
		CALL	DL1ms				
		POP	DX
		POP	BX
		POP	AX
		RET
DIR		ENDP

DL1ms		PROC	NEAR		
		PUSH	CX
		MOV	CX,500
		LOOP	$
		POP	CX
		RET
DL1ms		ENDP

GETKEY		PROC	NEAR	       
		PUSH	BX
		PUSH	DX
LK:		CALL	AllKey		;调用判有无闭合键子程序		
		JNE	LK1             ;有键按下则判断哪个按键

		CALL	DIR		;调用显示子程序
		JMP	LK             

;补充程序完成列扫描,得到按键在SEG_TAB中的值放入AL
LK1:		;用BL保存列线扫描口数值,从PB0开始
		;用BH保存列线值,从第0列开始
LK2:		;将BL写入B口列线控制端
		;读C口行线控制端
		;PC0不等于0转向判断PC1是否等于0
	        ;PC0等于0表示0行有键闭合,用BH存放按键值
		;PC0不等于0且PC1等于0表示01行有键闭合，用BH存放按键值等于BH+08H	

		;在PC0或PC1等于0的情况下(有键按下)需等待按键释放??-->CALL ALLKEY
		;按键释放了将保存在BH中的按键值-->AL,寄存器出栈,返回

		;PC0和PC1都不等于0则表示该列无按键按下需要扫描下一列:
		;	(BH列计数器+1,判断是否扫描到最后一列,
		;	 不是最后一列则将BL循环左移一位JMP LK2继续扫描,
		;	 如果是最后一列表示扫描结束寄存器出栈,返回)

GETKEY		ENDP


AllKey		PROC	NEAR            ;判断键盘是否有按键闭合
		;考虑哪些寄存器需要保护
		;全"0"->写B口列线控制端,列线控制端低电平有效
		;
		;
		;读C口数据		 
		;
		;
		;取C口低二位和00000011b比较
		RET
AllKey		ENDP
				
		END	START
