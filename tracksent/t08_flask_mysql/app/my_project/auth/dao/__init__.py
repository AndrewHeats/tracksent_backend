from .orders.driver_dao import DriverDAO
from .orders.field_dao import FieldDAO
from .orders.process_dao import ProcessDAO
from .orders.type_dao import TypeDAO
from .orders.vehicle_dao import VehicleDAO


field_dao = FieldDAO()
process_dao = ProcessDAO()
type_dao = TypeDAO()
vehicle_dao = VehicleDAO()
driver_dao = DriverDAO()

