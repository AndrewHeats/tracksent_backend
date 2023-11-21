

from flask import Flask

from .error_handler import err_handler_bp



def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.field_route import field_bp
    from .orders.process_route import process_bp
    from .orders.type_route import type_bp
    from .orders.vehicle_route import vehicle_bp
    from .orders.driver_route import driver_bp

    app.register_blueprint(driver_bp)
    app.register_blueprint(vehicle_bp)
    app.register_blueprint(type_bp)
    app.register_blueprint(process_bp)
    app.register_blueprint(field_bp)