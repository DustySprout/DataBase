from .models import *

from flask import current_app



class AccessPointsDAO:
    @staticmethod
    def get_all_access_points():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM company_inventory.access_points;")
            access_points = [AccessPoints(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching access points: {e}")
            access_points = []
        return access_points
    
    @staticmethod
    def get_access_point_by_id(access_point_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM company_inventory.access_points WHERE id = %s", (access_point_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching access point by id: {e}")
            row = None
        return AccessPoints(*row).to_dict() if row else None
    
    @staticmethod
    def add_access_point(serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO company_inventory.access_points (serial_number, model) VALUES (%s, %s)", (serial_number, model))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding access point: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_access_point(access_point_id, serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE company_inventory.access_points SET serial_number = %s, model = %s WHERE id = %s", (serial_number, model, access_point_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating access point: {e}")
            current_app.mysql.connection.rollback()
    
    @staticmethod
    def delete_access_point(access_point_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM company_inventory.access_points WHERE id = %s", (access_point_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting access point: {e}")
            current_app.mysql.connection.rollback()


class ConfigurationsDAO:
    @staticmethod
    def get_all_configurations():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM configurations;")
            configurations = [Configurations(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching configurations: {e}")
            configurations = []
        return configurations
    
    @staticmethod
    def get_configuration_by_id(configuration_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM configurations WHERE id = %s", (configuration_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching configuration by id: {e}")
            row = None
        return Configurations(*row).to_dict() if row else None
    
    @staticmethod
    def add_configuration(processor, memory, disk, graphics_card):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO configurations (processor, memory, disk, graphics_card) VALUES (%s, %s, %s, %s)", (processor, memory, disk, graphics_card))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding configuration: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_configuration(configuration_id, processor, memory, disk, graphics_card):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE configurations SET processor = %s, memory = %s, disk = %s, graphics_card = %s WHERE id = %s", (processor, memory, disk, graphics_card, configuration_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating configuration: {e}")
            current_app.mysql.connection.rollback()
    
    @staticmethod
    def delete_configuration(configuration_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM configurations WHERE id = %s", (configuration_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting configuration: {e}")
            current_app.mysql.connection.rollback()


class ComputersDAO:
    @staticmethod
    def get_all_computers():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM computers;")
            computers = [Computers(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching computers: {e}")
            computers = []
        return computers
    
    @staticmethod
    def get_computer_by_id(computer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM computers WHERE id = %s", (computer_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching computer by id: {e}")
            row = None
        return Computers(*row).to_dict() if row else None
    
    @staticmethod
    def add_computer(serial_number, type, model, configuration_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO computers (serial_number, type, model, configuration_id) VALUES (%s, %s, %s, %s)", (serial_number, type, model, configuration_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding computer: {e}")
            current_app.mysql.connection.rollback()
            
    @staticmethod
    def update_computer(computer_id, serial_number, type, model, configuration_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE computers SET serial_number = %s, type = %s, model = %s, configuration_id = %s WHERE id = %s", (serial_number, type, model, configuration_id, computer_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating computer: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_computer(computer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM computers WHERE id = %s", (computer_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting computer: {e}")
            current_app.mysql.connection.rollback()


class EmployeesDAO:
    @staticmethod
    def get_all_employees():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employees;")
            employees = [Employees(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching employees: {e}")
            employees = []
        return employees
    
    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching employee by id: {e}")
            row = None
        return Employees(*row).to_dict() if row else None
    
    @staticmethod
    def add_employee(first_name, last_name, email, phone):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO employees (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, phone))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding employee: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_employee(employee_id, first_name, last_name, email, phone):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE employees SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s", (first_name, last_name, email, phone, employee_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating employee: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_employee(employee_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting employee: {e}")
            current_app.mysql.connection.rollback()


class OfficesDAO:
    @staticmethod
    def get_all_offices():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM offices;")
            offices = [Offices(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching offices: {e}")
            offices = []
        return offices
    
    @staticmethod
    def get_office_by_id(office_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM offices WHERE id = %s", (office_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching office by id: {e}")
            row = None
        return Offices(*row).to_dict() if row else None
    
    @staticmethod
    def add_office(name, address):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO offices (name, address) VALUES (%s, %s)", (name, address))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding office: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_office(office_id, name, address):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE offices SET name = %s, address = %s WHERE id = %s", (name, address, office_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating office: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_office(office_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM offices WHERE id = %s", (office_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting office: {e}")
            current_app.mysql.connection.rollback()


class MonitorsDAO:
    @staticmethod
    def get_all_monitors():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM monitors;")
            monitors = [Monitors(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching monitors: {e}")
            monitors = []
        return monitors
    
    @staticmethod
    def get_monitor_by_id(monitor_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM monitors WHERE id = %s", (monitor_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching monitor by id: {e}")
            row = None
        return Monitors(*row).to_dict() if row else None

    @staticmethod
    def add_monitor(serial_number, model, screen_size):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO monitors (serial_number, model, screen_size) VALUES (%s, %s, %s)", (serial_number, model, screen_size))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding monitor: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_monitor(monitor_id, serial_number, model, screen_size):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE monitors SET serial_number = %s, model = %s, screen_size = %s WHERE id = %s", (serial_number, model, screen_size, monitor_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating monitor: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_monitor(monitor_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM monitors WHERE id = %s", (monitor_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting monitor: {e}")
            current_app.mysql.connection.rollback()


class PrintersDAO:
    @staticmethod
    def get_all_printers():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM printers;")
            printers = [Printers(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching printers: {e}")
            printers = []
        return printers
    
    @staticmethod
    def get_printer_by_id(printer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM printers WHERE id = %s", (printer_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching printer by id: {e}")
            row = None
        return Printers(*row).to_dict() if row else None
    
    @staticmethod
    def add_printer(serial_number, model, type):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO printers (serial_number, model, type) VALUES (%s, %s, %s)", (serial_number, model, type))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding printer: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_printer(printer_id, serial_number, model, type):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE printers SET serial_number = %s, model = %s, type = %s WHERE id = %s", (serial_number, model, type, printer_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating printer: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_printer(printer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM printers WHERE id = %s", (printer_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting printer: {e}")
            current_app.mysql.connection.rollback()


class RoutersDAO:
    @staticmethod
    def get_all_routers():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM routers;")
            routers = [Routers(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching routers: {e}")
            routers = []
        return routers
    
    @staticmethod
    def get_router_by_id(router_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM routers WHERE id = %s", (router_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching router by id: {e}")
            row = None
        return Routers(*row).to_dict() if row else None
    
    @staticmethod
    def add_router(serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO routers (serial_number, model) VALUES (%s, %s)", (serial_number, model))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding router: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_router(router_id, serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE routers SET serial_number = %s, model = %s WHERE id = %s", (serial_number, model, router_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating router: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_router(router_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM routers WHERE id = %s", (router_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting router: {e}")
            current_app.mysql.connection.rollback()



class IpPhonesDAO:
    @staticmethod
    def get_all_ip_phones():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM ip_phones;")
            ip_phones = [IpPhones(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching ip phones: {e}")
            ip_phones = []
        return ip_phones

    @staticmethod
    def get_ip_phone_by_id(ip_phone_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM ip_phones WHERE id = %s", (ip_phone_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching ip phone by id: {e}")
            row = None
        return IpPhones(*row).to_dict() if row else None
    
    @staticmethod
    def add_ip_phone(serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO ip_phones (serial_number, model) VALUES (%s, %s)", (serial_number, model))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding ip phone: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_ip_phone(ip_phone_id, serial_number, model):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE ip_phones SET serial_number = %s, model = %s WHERE id = %s", (serial_number, model, ip_phone_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating ip phone: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_ip_phone(ip_phone_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM ip_phones WHERE id = %s", (ip_phone_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting ip phone: {e}")
            current_app.mysql.connection.rollback()


class EmployeeEquipmentDAO:
    @staticmethod
    def get_all_employee_equipment():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employee_equipment;")
            employee_equipment = [EmployeeEquipment(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching employee equipment: {e}")
            employee_equipment = []
        return employee_equipment
    
    @staticmethod
    def get_employee_equipment_by_id(employee_equipment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM employee_equipment WHERE id = %s", (employee_equipment_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching employee equipment by id: {e}")
            row = None
        return EmployeeEquipment(*row).to_dict() if row else None
    
    @staticmethod
    def add_employee_equipment(employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO employee_equipment (employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding employee equipment: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_employee_equipment(employee_equipment_id, employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE employee_equipment SET employee_id = %s, computer_id = %s, monitor_id = %s, printer_id = %s, router_id = %s, access_point_id = %s, ip_phone_id = %s WHERE id = %s", (employee_id, computer_id, monitor_id, printer_id, router_id, access_point_id, ip_phone_id, employee_equipment_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating employee equipment: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_employee_equipment(employee_equipment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM employee_equipment WHERE id = %s", (employee_equipment_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting employee equipment: {e}")
            current_app.mysql.connection.rollback()


class OfficeEquipmentDAO:
    @staticmethod
    def get_all_office_equipment():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM office_equipment;")
            office_equipment = [OfficeEquipment(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching office equipment: {e}")
            office_equipment = []
        return office_equipment
    
    @staticmethod
    def get_office_equipment_by_id(office_equipment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM office_equipment WHERE id = %s", (office_equipment_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching office equipment by id: {e}")
            row = None
        return OfficeEquipment(*row).to_dict() if row else None
    
    @staticmethod
    def add_office_equipment(office_id, printer_id, router_id, access_point_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO office_equipment (office_id, printer_id, router_id, access_point_id) VALUES (%s, %s, %s, %s)", (office_id, printer_id, router_id, access_point_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding office equipment: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def update_office_equipment(office_equipment_id, office_id, printer_id, router_id, access_point_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE office_equipment SET office_id = %s, printer_id = %s, router_id = %s, access_point_id = %s WHERE id = %s", (office_id, printer_id, router_id, access_point_id, office_equipment_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating office equipment: {e}")
            current_app.mysql.connection.rollback()

    @staticmethod
    def delete_office_equipment(office_equipment_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM office_equipment WHERE id = %s", (office_equipment_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting office equipment: {e}")
            current_app.mysql.connection.rollback()


class SelectDAO:
    @staticmethod
    def first():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                        SELECT 
                            o.name AS office_name,
                            e.first_name,
                            e.last_name
                        FROM 
                            company_inventory.offices o
                        LEFT JOIN 
                            company_inventory.employee_equipment ee ON o.id = ee.office_id
                        LEFT JOIN 
                            company_inventory.employees e ON ee.employee_id = e.id
                        ORDER BY 
                            o.name, e.last_name;
                        """)
            employee_equipment = [row for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching employee equipment: {e}")
            employee_equipment = []
        return employee_equipment
    
    @staticmethod
    def second():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("""
                    SELECT 
                        e.first_name,
                        e.last_name,
                        ee.equipment_type,
                        CASE ee.equipment_type
                            WHEN 'Monitor' THEN m.model
                            WHEN 'Printer' THEN p.model
                            WHEN 'Router' THEN r.model
                            WHEN 'IP Phone' THEN ip.model
                            WHEN 'Access Point' THEN ap.model
                            ELSE 'Unknown'
                        END AS equipment_model
                    FROM 
                        company_inventory.employee_equipment ee
                    JOIN 
                        company_inventory.employees e ON ee.employee_id = e.id
                    LEFT JOIN 
                        company_inventory.monitors m ON ee.monitors_id = m.id
                    LEFT JOIN 
                        company_inventory.printers p ON ee.printers_id = p.id
                    LEFT JOIN 
                        company_inventory.routers r ON ee.routers_id = r.id
                    LEFT JOIN 
                        company_inventory.ip_phones ip ON ee.ip_phones_id = ip.id
                    LEFT JOIN 
                        company_inventory.access_points ap ON ee.access_points_id = ap.id
                    ORDER BY 
                        e.last_name, ee.equipment_type;
                    """)
            office_equipment = [row for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching office equipment: {e}")
            office_equipment = []
        return office_equipment
    