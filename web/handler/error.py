
class Error(object):
    ERROR_OK = 0
    ERROR_GET_TASK_LIST = 1
    ERROR_GET_TASK_ADD = 2
    ERROR_GET_TASK_PAGE_PARAM_ERROR = 3
    ERROR_GET_TASK_ADD_FREQUENTLY = 4
    error = (
        {'type': 'ERROR_OK', 'description': ''},
        {'type': 'ERROR_GET_TASK_LIST', 'description': '获取任务列表出错'},
        {'type': 'ERROR_GET_TASK_ADD', 'description': '新增任务出错'},
        {'type': 'ERROR_GET_TASK_PAGE_PARAM_ERROR', 'description': '获取任务列表页码参数错误'},
        {'type': 'ERROR_GET_TASK_ADD_FREQUENTLY', 'description': '添加抓取任务过于频繁'},
    )

    @staticmethod
    def get_description(int_type):
        return Error.error[int_type]['description']
