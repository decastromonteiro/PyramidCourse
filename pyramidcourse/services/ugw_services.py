# coding=utf-8
import ipaddress
import re


class UGW:
    def ssh_session(self):
        pass

    @staticmethod
    def summarize_ipv4(mml_file='F:\Estudos\PyramidCourse\pyramidcourse\db\ip'):
        ipv4_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        with open(mml_file) as fin:
            ip_list = list()
            for lines in fin:
                if lines.strip().startswith('section'):
                    ip_list.append(re.findall(pattern=ipv4_pattern, string=lines))

        networks = list()
        for ls in ip_list:
            networks.extend(ipaddress.summarize_address_range(
                ipaddress.IPv4Address(ls[0]),
                ipaddress.IPv4Address(ls[-1])
            ))

        aggregate = [str(network) for network in ipaddress.collapse_addresses(networks)]

        return aggregate

    @staticmethod
    def summarize_ipv6(mml_file):
        ipv6_pattern = r'.*prefix\s\d\s*([^\n\r]*)'
        ipv6_list = list()
        with open(mml_file) as fin:
            ip_list = list()
            for lines in fin:
                if lines.strip().startswith('prefix'):
                    ip_list.append(re.findall(pattern=ipv6_pattern, string=lines))
        for ls in ip_list:
            for txt in ls:
                ip_range = txt.strip().split()
                ipv6_list.append(ip_range)
        networks = list()
        for ls in ipv6_list:
            networks.extend(ipaddress.summarize_address_range(
                ipaddress.IPv6Address(ls[0]),
                ipaddress.IPv6Address(ls[-1])
            ))

        aggregate = [str(network) for network in ipaddress.collapse_addresses(networks)]

        return aggregate


def main():
    u = UGW()
    teste = u.summarize_ipv6('F:\Estudos\PyramidCourse\pyramidcourse\db\ip')
    for net in teste:
        print(net)


if __name__ == '__main__':
    main()
