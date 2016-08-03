from struct import calcsize
from ryu.lib import type_desc
from ryu.ofproto import oxm_fields
from ryu.ofproto import ofproto_utils

from ryu.ofproto.ofproto_common import OFP_HEADER_SIZE
OFP_OXM_EXPERIMENTER_HEADER_SIZE = 8

BEBA_EXPERIMENTER_ID = 0xBEBABEBA

# state ofp_exp_msg_state_mod
OFP_EXP_STATE_MOD_PACK_STR='!Bx'
OFP_EXP_STATE_MOD_SIZE =18
assert (calcsize(OFP_EXP_STATE_MOD_PACK_STR)) + OFP_HEADER_SIZE + OFP_OXM_EXPERIMENTER_HEADER_SIZE == OFP_EXP_STATE_MOD_SIZE

# struct ofp_exp_stateful_table_config
OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_PACK_STR='!BB'
OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_SIZE = 2
assert (calcsize(OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_PACK_STR)== OFP_EXP_STATE_MOD_STATEFUL_TABLE_CONFIG_SIZE)

# struct ofp_exp_set_extractor
MAX_FIELD_COUNT=6
OFP_EXP_STATE_MOD_EXTRACTOR_PACK_STR='!B3xI'
OFP_EXP_STATE_MOD_EXTRACTOR_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_EXTRACTOR_PACK_STR) == OFP_EXP_STATE_MOD_EXTRACTOR_SIZE)

# struct ofp_exp_set_flow_state
MAX_KEY_LEN=48
OFP_EXP_STATE_MOD_SET_FLOW_STATE_PACK_STR='!B3xIIIIIII'
OFP_EXP_STATE_MOD_SET_FLOW_ENTRY_SIZE = 32
assert (calcsize(OFP_EXP_STATE_MOD_SET_FLOW_STATE_PACK_STR) == OFP_EXP_STATE_MOD_SET_FLOW_ENTRY_SIZE)

# struct ofp_exp_del_flow_state
OFP_EXP_STATE_MOD_DEL_FLOW_STATE_PACK_STR='!B3xI'
OFP_EXP_STATE_MOD_DEL_FLOW_ENTRY_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_DEL_FLOW_STATE_PACK_STR) == OFP_EXP_STATE_MOD_DEL_FLOW_ENTRY_SIZE)
 
# state ofp_exp_set_global_state
OFP_EXP_STATE_MOD_SET_GLOBAL_STATE_PACK_STR='!II'
OFP_EXP_STATE_MOD_SET_GLOBAL_ENTRY_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_SET_GLOBAL_STATE_PACK_STR)) == OFP_EXP_STATE_MOD_SET_GLOBAL_ENTRY_SIZE

# struct ofp_exp_action_set_state
OFP_EXP_ACTION_SET_STATE_PACK_STR = '!I4xIIB3xIIIII'
OFP_EXP_ACTION_SET_STATE_SIZE = 40
assert calcsize(OFP_EXP_ACTION_SET_STATE_PACK_STR) == OFP_EXP_ACTION_SET_STATE_SIZE

# struct ofp_exp_action_set_global_state
OFP_EXP_ACTION_SET_GLOBAL_STATE_PACK_STR = '!I4xII'
OFP_EXP_ACTION_SET_GLOBAL_STATE_SIZE = 16
assert calcsize(OFP_EXP_ACTION_SET_GLOBAL_STATE_PACK_STR) == OFP_EXP_ACTION_SET_GLOBAL_STATE_SIZE

# struct ofp_exp_action_set_data_variable
OFP_EXP_ACTION_SET_DATA_VARIABLE_PACK_STR = '!I4xHBBB3xBBBBbbbbI4x'
OFP_EXP_ACTION_SET_DATA_VARIABLE_SIZE = 32
assert calcsize(OFP_EXP_ACTION_SET_DATA_VARIABLE_PACK_STR) == OFP_EXP_ACTION_SET_DATA_VARIABLE_SIZE

# struct ofp_state_stats_request
OFP_STATE_STATS_REQUEST_0_PACK_STR = '!BB2xI'
OFP_STATE_STATS_REQUEST_0_SIZE = 8
assert (calcsize(OFP_STATE_STATS_REQUEST_0_PACK_STR) ==
        OFP_STATE_STATS_REQUEST_0_SIZE)

# struct ofp_state_stats
OFP_STATE_STATS_0_PACK_STR = '!HBxIII'
OFP_STATE_STATS_0_SIZE = 16
assert calcsize(OFP_STATE_STATS_0_PACK_STR) == OFP_STATE_STATS_0_SIZE
OFP_STATE_STATS_ENTRY_SIZE = 56
OFP_STATE_STATS_1_PACK_STR = '!IIII'
OFP_STATE_STATS_1_SIZE = 16
assert calcsize(OFP_STATE_STATS_1_PACK_STR) == OFP_STATE_STATS_1_SIZE
OFP_STATE_STATS_SIZE = OFP_STATE_STATS_0_SIZE + 4*MAX_FIELD_COUNT + OFP_STATE_STATS_ENTRY_SIZE + OFP_STATE_STATS_1_SIZE

# struct ofp_exp_msg_pkttmp_mod
OFP_EXP_PKTTMP_MOD_PACK_STR='!Bx'
OFP_EXP_PKTTMP_MOD_SIZE =18
assert (calcsize(OFP_EXP_PKTTMP_MOD_PACK_STR)) + OFP_HEADER_SIZE + OFP_OXM_EXPERIMENTER_HEADER_SIZE == OFP_EXP_PKTTMP_MOD_SIZE

# struct ofp_exp_add_pkttmp
OFP_EXP_PKTTMP_MOD_ADD_PKTTMP_PACK_STR='!I4x'
OFP_EXP_PKTTMP_MOD_ADD_PKTTMP_SIZE = 8
assert (calcsize(OFP_EXP_PKTTMP_MOD_ADD_PKTTMP_PACK_STR) == OFP_EXP_PKTTMP_MOD_ADD_PKTTMP_SIZE)

# struct ofp_exp_del_pkttmp
OFP_EXP_PKTTMP_MOD_DEL_PKTTMP_PACK_STR='!I4x'
OFP_EXP_PKTTMP_MOD_DEL_PKTTMP_SIZE = 8
assert (calcsize(OFP_EXP_PKTTMP_MOD_DEL_PKTTMP_PACK_STR) == OFP_EXP_PKTTMP_MOD_DEL_PKTTMP_SIZE)

# struct ofp_instruction_in_switch_pkt_gen
OFP_INSTRUCTION_INSWITCH_PKT_GEN_PACK_STR = '!HHII4xI4x'
OFP_INSTRUCTION_INSWITCH_PKT_GEN_SIZE = 24
assert (calcsize(OFP_INSTRUCTION_INSWITCH_PKT_GEN_PACK_STR) ==
        OFP_INSTRUCTION_INSWITCH_PKT_GEN_SIZE)

# struct ofp_exp_set_header_field_extractor
MAX_HEADER_FIELDS=8
OFP_EXP_STATE_MOD_SET_HEADER_EXTRACTOR_PACK_STR='!BB2xI'
OFP_EXP_STATE_MOD_SET_HEADER_EXTRACTOR_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_SET_HEADER_EXTRACTOR_PACK_STR) == OFP_EXP_STATE_MOD_SET_HEADER_EXTRACTOR_SIZE)

OPCODE_SUM = 0
OPCODE_SUB = 1
OPCODE_MUL = 2
OPCODE_DIV = 3
OPCODE_AVG = 4
OPCODE_VAR = 5
OPCODE_EWMA = 6
OPCODE_POLY_SUM = 7

# struct ofp_exp_set_condition
MAX_CONDITIONS_NUM=8
MAX_FLOW_DATA_VAR_NUM=6
MAX_GLOBAL_DATA_VAR_NUM=8
OPERAND_TYPE_FLOW_DATA_VAR=0
OPERAND_TYPE_GLOBAL_DATA_VAR=1
OPERAND_TYPE_HEADER_FIELD=2
OPERAND_TYPE_CONSTANT=3
CONDITION_GT=0
CONDITION_LT=1
CONDITION_GTE=2
CONDITION_LTE=3
CONDITION_EQ=4
CONDITION_NEQ=5
OFP_EXP_STATE_MOD_SET_CONDITION_PACK_STR='!BBBBBB2x'
OFP_EXP_STATE_MOD_SET_CONDITION_SIZE = 8
assert (calcsize(OFP_EXP_STATE_MOD_SET_CONDITION_PACK_STR) == OFP_EXP_STATE_MOD_SET_CONDITION_SIZE)

# struct ofp_exp_set_global_data_var
OFP_EXP_STATE_MOD_SET_GLOBAL_DATA_VAR_PACK_STR='!BB2xII'
OFP_EXP_STATE_MOD_SET_GLOBAL_DATA_VAR_SIZE = 12
assert (calcsize(OFP_EXP_STATE_MOD_SET_GLOBAL_DATA_VAR_PACK_STR) == OFP_EXP_STATE_MOD_SET_GLOBAL_DATA_VAR_SIZE)

# struct ofp_exp_set_flow_data_var
OFP_EXP_STATE_MOD_SET_FLOW_DATA_VAR_PACK_STR='!BB2xIII'
OFP_EXP_STATE_MOD_SET_FLOW_DATA_VAR_SIZE = 16
assert (calcsize(OFP_EXP_STATE_MOD_SET_FLOW_DATA_VAR_PACK_STR) == OFP_EXP_STATE_MOD_SET_FLOW_DATA_VAR_SIZE)

# enum ofp_exp_messages
OFPT_EXP_STATE_MOD = 0
OFPT_EXP_PKTTMP_MOD = 1
OFPT_EXP_STATE_CHANGED = 2
OFPT_EXP_FLOW_NOTIFICATION = 3

# enum ofp_state_mod_command 
OFPSC_EXP_STATEFUL_TABLE_CONFIG = 0
OFPSC_EXP_SET_L_EXTRACTOR   = 1
OFPSC_EXP_SET_U_EXTRACTOR   = 2
OFPSC_EXP_SET_FLOW_STATE    = 3
OFPSC_EXP_DEL_FLOW_STATE    = 4
OFPSC_EXP_SET_GLOBAL_STATE      = 5
OFPSC_EXP_RESET_GLOBAL_STATE    = 6
OFPSC_EXP_SET_HEADER_FIELD_EXTRACTOR= 7
OFPSC_EXP_SET_CONDITION = 8
OFPSC_EXP_SET_GLOBAL_DATA_VAR = 9
OFPSC_EXP_SET_FLOW_DATA_VAR = 10

# enum ofp_pkttmp_mod_command
OFPSC_ADD_PKTTMP = 0
OFPSC_DEL_PKTTMP = 1

# enum ofp_exp_instructions 
OFPIT_IN_SWITCH_PKT_GEN = 0

# enum ofp_exp_actions
OFPAT_EXP_SET_STATE = 0
OFPAT_EXP_SET_GLOBAL_STATE  = 1
OFPAT_EXP_SET_DATA_VAR  = 2

# enum ofp_stats_extension_commands
OFPMP_EXP_STATE_STATS = 0
OFPMP_EXP_GLOBAL_STATE_STATS = 1

# enum ofp_error_type
OFPET_EXPERIMENTER = 0xffff

# enum ofp_experimenter_code
OFPEC_EXP_STATE_MOD_FAILED       = 0
OFPEC_EXP_STATE_MOD_BAD_COMMAND  = 1
OFPEC_EXP_SET_EXTRACTOR          = 2
OFPEC_EXP_SET_FLOW_STATE         = 3
OFPEC_EXP_DEL_FLOW_STATE         = 4
OFPEC_BAD_EXP_MESSAGE            = 5
OFPEC_BAD_EXP_ACTION             = 6
OFPEC_BAD_EXP_LEN                = 7
OFPEC_BAD_TABLE_ID               = 8
OFPEC_BAD_MATCH_WILDCARD         = 9
OFPEC_BAD_EXP_INSTRUCTION        = 10
OFPEC_EXP_PKTTMP_MOD_FAILED      = 11
OFPEC_EXP_PKTTMP_MOD_BAD_COMMAND = 12
OFPEC_BAD_EXTRACTOR_ID           = 13
OFPEC_BAD_CONDITION_ID           = 14
OFPEC_BAD_CONDITION              = 15
OFPEC_BAD_OPERAND_TYPE           = 16
OFPEC_BAD_FLOW_DATA_VAR_ID       = 17
OFPEC_BAD_GLOBAL_DATA_VAR_ID     = 18
OFPEC_BAD_HEADER_FIELD_SIZE      = 19
OFPEC_BAD_OPCODE                 = 20
OFPEC_BAD_HEADER_EXTRACTOR       = 21
OFPEC_BAD_SOURCE_TYPE            = 22

# Beba experimenter fields
oxm_types = [
    oxm_fields.BebaExperimenter('global_state', 0, type_desc.Int4),
    oxm_fields.BebaExperimenter('state', 1, type_desc.Int4),
    oxm_fields.BebaExperimenter('condition0', 2, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition1', 3, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition2', 4, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition3', 5, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition4', 6, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition5', 7, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition6', 8, type_desc.Int1),
    oxm_fields.BebaExperimenter('condition7', 9, type_desc.Int1),
    oxm_fields.BebaExperimenter('timestamp', 10, type_desc.Int4),
    oxm_fields.BebaExperimenter('random', 11, type_desc.Int2),
    oxm_fields.BebaExperimenter('pkt_len', 12, type_desc.Int2)
]

# generate utility methods
ofproto_utils.generate(__name__)

def _oxm_tlv_header(class_, field, hasmask, length):
    return (class_ << 16) | (field << 9) | (hasmask << 8) | length


def oxm_tlv_exp_header(field, length):
    return _oxm_tlv_header(0xFFFF, field, 0, length+4)

# Generate OXM_EXP_* attributes
import sys
mod = sys.modules[__name__]
for i in oxm_types:
    uk = i.name.upper()
    ofpxmt = i.oxm_field
    td = i.type
    setattr(mod, 'OXM_EXP_' + uk, mod.oxm_tlv_exp_header(ofpxmt, td.size))