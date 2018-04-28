import unittest
import HTMLReport
from HTMLReport import logger
from testcase.knowledge_controller.knowledge_controller import KnowledgeController

# 测试套件
suite = unittest.TestSuite ()
# 测试用例加载器
loader = unittest.TestLoader ()
# 把测试用例加载到测试套件中
suite.addTests (loader.loadTestsFromTestCase (KnowledgeController))

# 测试用例执行器

runner = HTMLReport.TestRunner (report_file_name='reports',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                output_path='report/' ,
                                title='CHATBOT API 测试报告' ,
                                description='测试用例执行情况' ,
                                thread_count=1 ,  # 并发线程数量（无序执行测试），默认数量 1
                                sequential_execution=False ,  # 是否按照套件添加(addTests)顺序执行，
                                # 会等待一个addTests执行完成，再执行下一个，默认 False
                                # 如果用例中存在 tearDownClass ，建议设置为True，
                                # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                # lang='en',
                                lang='cn'  # 支持中文与英文，默认中文
                                )
# 执行测试用例套件
runner.run (suite)
logger ().info ("测试")
logger ().debug ("测试")
logger ().warning ("测试")
logger ().error ("测试")
logger ().critical ("测试")
