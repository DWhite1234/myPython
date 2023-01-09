import logging
import logging.config as config
import os
# 定义日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
# 定义日志输出格式 结束

# 自定义文件路径
logfile_path = '/Users/zhongtao/disk/workspace/mine/myPython/log/demo.log'
if not os.path.exists(logfile_path):
    # os.mknod(logfile_path)
    open(logfile_path, 'a').close()


# log配置字典
LOGGING_DIC = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'standard': {
          'format': standard_format
      },
      'simple': {
          'format': simple_format
      },
  },
  'filters': {},  # 过滤日志
  'handlers': {
      #打印到终端的日志
      'console': {
          'level': 'INFO',
          'class': 'logging.StreamHandler',  # 打印到屏幕
          'formatter': 'simple'
      },
      #打印到文件的日志,收集info及以上的日志
      'default': {
          'level': 'DEBUG',
          'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
          'formatter': 'standard',
          'filename': logfile_path,  # 日志文件
          'maxBytes': 1024*1024*5,  # 日志大小 5M
          'backupCount': 5,
          'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
      },
  },
  'loggers': {
      #logging.getLogger(__name__)拿到的logger配置
      '': {
          'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
          'level': 'DEBUG',
          'propagate': True,  # 向上（更高level的logger）传递
      },  # 当键不存在的情况下 (key设为空字符串)默认都会使用该k:v配置
      # '注册记录': {
      #     'handlers': ['console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
      #     'level': 'WARNING',
      #     'propagate': True,  # 向上（更高level的logger）传递
      # },  # 当键不存在的情况下 (key设为空字符串)默认都会使用该k:v配置
  },
}
config.dictConfig(LOGGING_DIC)
log = logging.getLogger("注册")
