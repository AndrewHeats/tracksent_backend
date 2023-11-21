
from .orders.driver_controller import DriverController
from .orders.field_controller import FieldController
from .orders.process_controller import ProcessController
from .orders.type_controller import TypeController
from .orders.vehicle_controller import VehicleController

field_controller = FieldController()
process_controller = ProcessController()
type_controller = TypeController()
vehicle_controller = VehicleController()
driver_controller = DriverController()