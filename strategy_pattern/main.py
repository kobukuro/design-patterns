from strategy_pattern.context import Context
from strategy_pattern.strategy.concrete_strategy_a import ConcreteStrategyA
from strategy_pattern.strategy.concrete_strategy_b import ConcreteStrategyB

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    print("Client: strategy is set to normal sorting.")
    # print(context.strategy)
    context.do_some_business_logic()
    print()

    context.strategy = ConcreteStrategyB()
    print("Client: strategy is set to reverse sorting.")
    # print(context.strategy)

    context.do_some_business_logic()
