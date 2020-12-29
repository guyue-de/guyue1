





from python_jianjian.lesson7 import read_case,api_fun,write_result
def excute_fun(filename,sheetname):
    cases=read_case(filename, sheetname)#调用函数
    for case in cases:
        case_id=case['case_id']
        url=case['url']
        data=case['data']
        expect=eval(case['expect'])
        expect_msg=expect['msg']
        print(case_id)
        print('期望结果为{}'.format(expect_msg))
        real_result=api_fun(url=url,data=data)#调用函数
        real_msg=real_result['msg']
        print('实际结果为{}'.format(real_msg))
        if expect_msg==real_msg:
            print('这第{}条测试用例通过！'.format(case_id))
            final_result='Passed'
        else:
            print('这第{}条测试用例不通过！'.format(case_id))
            final_result='Failed'
        write_result(filename,sheetname,case_id+1,8,final_result)#调用函数
        print('*'*15)

# excute_fun('C:\\Users\\wzfwzf108122\\PycharmProjects\\python\\test_data\\test_case_api.xlsx','register')
excute_fun('C:\\Users\\wzfwzf108122\\PycharmProjects\\python\\test_data\\test_case_api.xlsx','login')#调用函数

