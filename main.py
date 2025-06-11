from dependency_injector.wiring import inject, Provide
from cars import Container

@inject
def main (cars = Provide[Container.cars]) -> None:
    cars.run()

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    main()