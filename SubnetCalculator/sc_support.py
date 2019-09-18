import math
from Subnet import Subnet

def fill_byte(str_bin):
    bin_length = len(str_bin)
    for i in range(8-bin_length):
        str_bin = '0'+str_bin
    return  str_bin

def compare_bits(ip, sm):
    real_ip = ''
    for i in range(len(ip)):
        if ip[i] == sm[i]:
            if ip[i] == '1':
                real_ip = real_ip+'1'
            else:
                real_ip = real_ip+'0'
        else:
            real_ip = real_ip+'0'
    return  real_ip


def convert_binstr_to_dec(line):
    dec_octet = 0
    for i in range(len(line)):
        dec_octet += math.pow(2, 7-i)*int(line[i])
    return dec_octet

def turn_to_highest(tail,network):
    highest_ip = ''
    host_len = 8-len(tail)
    for i in range(host_len):
        highest_ip += network[i]
    for i in range(len(tail)):
        highest_ip += '1'
    return highest_ip
def bin_plus_one(str_bin):
    bigger_bin = ''
    for i in range(len(str_bin)):
        if i == len(str_bin)-1:
            bigger_bin += '1'
        else:
            bigger_bin += str_bin[i-1]
    return  bigger_bin

def bin_nega_one(str_bin):
    bigger_bin = ''
    for i in range(len(str_bin)):
        if i == len(str_bin)-1:
            bigger_bin += '0'
        else:
            bigger_bin += str_bin[i-1]
    return  bigger_bin


def calculate(ip, sm):
    subnet = Subnet()
    ip_parts = ip.split('.')
    sm_parts = sm.split('.')
    for i in range(len(ip_parts)):
        octet_ip = int(ip_parts[i])
        octet_sm = int(sm_parts[i])

        """Converting dec to bin"""
        bin_octet_ip = bin(octet_ip)
        bin_octet_sm = bin(octet_sm)

        """Delete 0b which is set before binary value"""
        str_bin_octet_ip = str(bin_octet_ip).replace('0b', '')
        str_bin_octet_sm = str(bin_octet_sm).replace('0b', '')

        """filling bin becomes 8 bits"""
        str_bin_octet_ip = fill_byte(str_bin_octet_ip)
        str_bin_octet_sm = fill_byte(str_bin_octet_sm)

        """Calculate network address"""
        real_ip = compare_bits(str_bin_octet_ip, str_bin_octet_sm)
        bin_octet_ip = convert_binstr_to_dec(real_ip)
        str_dec_octet_ip = str(bin_octet_ip).replace(".0", "")
        subnet.bin_network = subnet.bin_network+real_ip
        subnet.dec_network = subnet.dec_network+str_dec_octet_ip


        """Calculate broadcast address"""
        bin_broadcast = ''
        if str_bin_octet_sm != '11111111':
            if str_bin_octet_sm != '00000000':
                tail_part = str_bin_octet_sm.replace('1', '')
                bin_broadcast = turn_to_highest(tail_part, real_ip)
            else:
                bin_broadcast = '11111111'
        else:
            bin_broadcast = real_ip
        subnet.bin_broadcast += bin_broadcast
        subnet.dec_broadcast += str(convert_binstr_to_dec(bin_broadcast)).replace(".0", "")

        """Calculate first address"""
        if i == len(ip_parts) - 1:
            subnet.bin_first_host += bin_plus_one(real_ip)
            subnet.dec_first_host += str(convert_binstr_to_dec(bin_plus_one(real_ip))).replace(".0", "")
        else:
            subnet.bin_first_host += real_ip
            subnet.dec_first_host += str(convert_binstr_to_dec(real_ip)).replace(".0", "")
                                                                                 
        """Calculate last address"""
        if i == len(ip_parts) - 1:
            subnet.bin_last_host += bin_nega_one(bin_broadcast)
            subnet.dec_last_host += str(convert_binstr_to_dec(bin_nega_one(bin_broadcast))).replace(".0", "")
        else:
            subnet.bin_last_host += bin_broadcast
            subnet.dec_last_host += str(convert_binstr_to_dec(bin_broadcast)).replace(".0", "")


        if i < len(ip_parts)-1:
            subnet.bin_network = subnet.bin_network+'.'
            subnet.dec_network = subnet.dec_network+'.'
            subnet.bin_broadcast = subnet.bin_broadcast +'.'
            subnet.dec_broadcast += '.'
            subnet.bin_first_host += '.'
            subnet.dec_first_host += '.'
            subnet.bin_last_host += '.'
            subnet.dec_last_host += '.'

    print('Network: '+subnet.dec_network+' , '+subnet.bin_network)
    print('Broadcast: ' + subnet.dec_broadcast + ' , ' + subnet.bin_broadcast)
    print('First host: ' + subnet.dec_first_host + ' , ' + subnet.bin_first_host)
    print('Last host: ' + subnet.dec_last_host + ' , ' + subnet.bin_last_host)