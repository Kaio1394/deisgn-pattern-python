from singleton_logger import SingletonLogger


singLogger = SingletonLogger.get_instance()
singLogger2 = SingletonLogger.get_instance()

if singLogger is singLogger2:
    print("Same instance.")

singLogger2.log("This is logged using a singleton logging system.")