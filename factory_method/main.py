from dynamic.dynamic_factory import DynamicFactory


factory = DynamicFactory()
instance = factory.create("GooglePayPayment")
instance.pay(1000)
