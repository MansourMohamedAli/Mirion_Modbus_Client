from pymodbus.client.tcp import ModbusTcpClient
import time

# Connect to the Modbus TCP server
# client = ModbusTcpClient('localhost', port=502)
client = ModbusTcpClient('127.0.0.1', port=502)
# client.connect()
# print(client.is_socket_open())
# Read the values from the Modbus registers
# coils = client.read_coils(address=0, count=100)
# discrete_inputs = client.read_discrete_inputs(address=0, count=100)
holding_registers = client.read_holding_registers(0, 1)
# input_registers = client.read_input_registers(0, 4)


# input_registers = client.read_input_registers(address=0, count=100)

# Should check for errors here... i.e.
# if coils.isError():
#     print('Error getting coils: {coils}')
#     raise Exception('Error getting coils: {coils}') # trying to display coils.bits would fail


# Print the values
# print("Coils:", coils.bits)
# print("Discrete Inputs:", discrete_inputs.bits)
print("Holding Registers:", holding_registers.registers)
# print("Input Registers:", input_registers.registers)


#Output to Mirions
if holding_registers.registers:
    mirionOut = holding_registers.registers
else:
    pass

# Close the Modbus TCP client
client.close()