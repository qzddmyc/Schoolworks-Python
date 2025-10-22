class Contact:
    def __init__(self):
        self.dict = {}

    def add(self, name: str, number: str) -> bool:
        if name in self.dict:
            return False
        self.dict[name] = number
        return True

    def query(self, name: str) -> str | None:
        return self.dict.get(name, None)

    def delete(self, name: str) -> bool:
        if name in self.dict:
            del self.dict[name]
            return True
        return False


contact = Contact()
while True:
    print('-' * 20)
    print("  1. 新增联系人\n  2. 查询联系人\n  3. 删除联系人\n  4. 退出")
    ipt = input("Your choice：")
    match ipt:
        case '1':
            name = input("请输入联系人姓名：")
            number = input("请输入联系人号码：")
            if contact.add(name, number):
                print("联系人添加成功")
            else:
                print("联系人已存在，添加失败")
        case '2':
            name = input("请输入需要查询的联系人姓名：")
            number = contact.query(name)
            if number:
                print(f"联系人号码为：{number}")
            else:
                print("联系人不存在")
        case '3':
            name = input("请输入需要删除的联系人姓名：")
            if contact.delete(name):
                print("联系人删除成功")
            else:
                print("联系人不存在，删除失败")
        case '4':
            print("退出成功")
            break
        case _:
            print("不合法的输入")
    input("回车键继续...")
