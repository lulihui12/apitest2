import requests


class TestdptAPi:
    id = 'wwe74f5c4f4abd49bf'
    secrete = 'LYCT9hnHtwA0qx9cbzxQAtiGC3s5q8T1J4HHB-M6xv8'

    def setup(self):
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = res.json()['access_token']

    def test_dptget(self):
        # 新建部门：测试部
        create_data = {
            "name": "测试部",
            "parentid": 1
        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=' + self.token,
                          json=create_data)
        print(r.json())
        self.id = r.json()["id"]
        # 查询部门列表
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}')
        print(r.json())
        # 判断部门列表中是否存在 测试部
        assert r.json()['department'][1]['name'] == "测试部"
        # 修改部门名称为 研发中心，
        update_data = {
            "id": self.id,
            "name": "研发中心"
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}',
                          json=update_data)
        print(r.json())
        assert r.json()["errcode"] == 0
        # 删除部门
        r = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}')
        print(r.json())
        assert r.json()["errcode"] == 0
