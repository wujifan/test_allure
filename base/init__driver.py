import yaml
import os


def ini_data(file_name, value_items):
    """
    读取测试用例数据
    :param file_name: 测试用例名称
    :param value_items: 测试用例中值的key值
    :return:
    """
    data_list = []
    if isinstance(file_name, str):
        if file_name.endswith('.yml'):
            file_path = os.getcwd() + os.sep + 'data' + os.sep + file_name
        else:
            file_path = os.getcwd() + os.sep + 'data' + os.sep + file_name + '.yml'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_test = yaml.load(f, Loader=yaml.Loader)   # 获取yaml中所有的数据
            for test_name, test_value_dict in data_test.get('test_data').items():   # 遍历测试名和测试用例数据
                test_value_list = []    # 定义空列表，用来存每一条测试用例数据
                for value in value_items:
                    test_value_list.append(test_value_dict.get(value))     # 将测试用例数据放入到列表中
                # print(test_value_list)
                data_list.append((test_name, *test_value_list))  # 将测试用例名和测试用例值放入到列表中
    except Exception as e:
        print(e)
    data_list.sort()
    # print(data_list)
    return data_list
