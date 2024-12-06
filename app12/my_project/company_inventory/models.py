class AccessPoints:
    def __init__(self, id, serial_number, model):
        self.id = id
        self.serial_number = serial_number
        self.model = model

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model
        }


class Configurations:
    def __init__(self, id, processor, memory, disk, graphics_card):
        self.id = id
        self.processor = processor
        self.memory = memory
        self.disk = disk
        self.graphics_card = graphics_card

    def to_dict(self):
        return {
            'id': self.id,
            'processor': self.processor,
            'memory': self.memory,
            'disk': self.disk,
            'graphics_card': self.graphics_card
        }


class Computers:
    def __init__(self, id, serial_number, type, model, configuration_id):
        self.id = id
        self.serial_number = serial_number
        self.type = type
        self.model = model
        self.configuration_id = configuration_id

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'type': self.type,
            'model': self.model,
            'configuration_id': self.configuration_id
        }


class Employees:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone
        }


class Offices:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
    

class Monitors:
    def __init__(self, id, serial_number, model, screen_size):
        self.id = id
        self.serial_number = serial_number
        self.model = model
        self.screen_size = screen_size

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model,
            'screen_size': self.screen_size
        }


class Printers:
    def __init__(self, id, serial_number, model, type):
        self.id = id
        self.serial_number = serial_number
        self.model = model
        self.type = type

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model,
            'type': self.type
        }


class Routers:
    def __init__(self, id, serial_number, model):
        self.id = id
        self.serial_number = serial_number
        self.model = model

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model
        }
    

class IpPhones:
    def __init__(self, id, serial_number, model):
        self.id = id
        self.serial_number = serial_number
        self.model = model

    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'model': self.model
        }


class EmployeeEquipment:
    def __init__(self, id, employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id):
        self.id = id
        self.employee_id = employee_id
        self.computer_id = computer_id
        self.monitor_id = monitor_id
        self.printer_id = printer_id
        self.router_id = router_id
        self.access_point_id = access_point_id
        self.ip_phone_id = ip_phone_id

    def to_dict(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'computer_id': self.computer_id,
            'monitor_id': self.monitor_id,
            'printer_id': self.printer_id,
            'router_id': self.router_id,
            'access_point_id': self.access_point_id,
            'ip_phone_id': self.ip_phone_id
        }


class OfficeEquipment:
    def __init__(self, id, office_id, printer_id, router_id, access_point_id):
        self.id = id
        self.office_id = office_id
        self.printer_id = printer_id
        self.router_id = router_id
        self.access_point_id = access_point_id

    def to_dict(self):
        return {
            'id': self.id,
            'office_id': self.office_id,
            'printer_id': self.printer_id,
            'router_id': self.router_id,
            'access_point_id': self.access_point_id
        }
