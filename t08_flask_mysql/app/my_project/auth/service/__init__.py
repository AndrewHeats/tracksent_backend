from .orders.driver_service import DriverService
from .orders.field_service import FieldService
from .orders.process_service import ProcessService
from .orders.type_service import TypeService
from .orders.vehicle_service import VehicleService

field_service = FieldService()
process_service = ProcessService()
type_service = TypeService()
vehicle_service = VehicleService()
driver_service = DriverService()
