# Copyright 2015
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_lib import constants

from neutron.common import constants as n_const

OF_STATE_NOT_TRACKED = "-trk"
OF_STATE_TRACKED = "+trk"
OF_STATE_NEW_NOT_ESTABLISHED = "+new-est"
OF_STATE_NOT_ESTABLISHED = "-est"
OF_STATE_ESTABLISHED = "+est"
OF_STATE_ESTABLISHED_NOT_REPLY = "+est-rel-rpl"
OF_STATE_ESTABLISHED_REPLY = "+est-rel+rpl"
OF_STATE_RELATED = "-new-est+rel-inv"
OF_STATE_INVALID = "+trk+inv"
OF_STATE_NEW = "+new"
OF_STATE_NOT_REPLY_NOT_NEW = "-new-rpl"

CT_MARK_NORMAL = '0x0'
CT_MARK_INVALID = '0x1'

REG_PORT = 5
REG_NET = 6

FW_BASE_EGRESS_TABLE = 64
FW_RULES_EGRESS_TABLE = 65
FW_ACCEPT_OR_INGRESS_TABLE = 66
FW_BASE_INGRESS_TABLE = 68
FW_RULES_INGRESS_TABLE = 69

OVS_FIREWALL_TABLES = (
    FW_BASE_EGRESS_TABLE,
    FW_RULES_EGRESS_TABLE,
    FW_ACCEPT_OR_INGRESS_TABLE,
    FW_BASE_INGRESS_TABLE,
    FW_RULES_INGRESS_TABLE,
)

PROTOCOLS_WITH_PORTS = (constants.PROTO_NAME_SCTP,
                        constants.PROTO_NAME_TCP,
                        constants.PROTO_NAME_UDP)

# Only map protocols that need special handling
REVERSE_IP_PROTOCOL_MAP_WITH_PORTS = {
    constants.IP_PROTOCOL_MAP[proto]: proto for proto in
    PROTOCOLS_WITH_PORTS}

ethertype_to_dl_type_map = {
    constants.IPv4: n_const.ETHERTYPE_IP,
    constants.IPv6: n_const.ETHERTYPE_IPV6,
}
