from collections import namedtuple

TS3Vector = namedtuple('TS3Vecor', 'x y')

PLUGIN_MENU_BUFSZ = 128
PLUGIN_HOTKEY_BUFSZ = 128

ERROR_parameter_quote = 0x0600

ERROR_sound_read_wave = 0x0914

ERROR_accounting_to_many_starts = 0x0b0e

ERROR_server_modal_quit = 0x040c

ERROR_client_cannot_verify_now = 0x020e

ERROR_file_already_exists = 0x0802

ERROR_server_deployment_active = 0x0405

ERROR_sound_handler_has_device = 0x0908

ERROR_provisioning_internal_tries_exceeded = 0x1106

ERROR_permission_invalid_size = 0x0a05

ERROR_permission_duplicate_entry = 0x0a01

ERROR_sound_invalid_capture_device = 0x0909

ERROR_file_transfer_server_quota_exceeded = 0x0814

ERROR_serverlibrary_not_initialised = 0x070a

ERROR_provisioning_no_slots_available = 0x1102

ERROR_parameter_convert = 0x0604

ERROR_permission_invalid_group_id = 0x0a00

ERROR_client_could_not_validate_identity = 0x0207

ERROR_provisioning_unknown_ip_location = 0x1105

ERROR_provisioning_not_initialized = 0x1113

ERROR_accounting_license_file_invalid = 0x0b09

ERROR_client_already_subscribed = 0x0205

ERROR_server_is_virtual = 0x0407

ERROR_channel_name_inuse = 0x0303

ERROR_server_duplicate_running = 0x040e

ERROR_file_transfer_reset = 0x0816

ERROR_no_network_port_available = 0x0102

ERROR_dont_notify = 0x0004

ERROR_voip_invalid_connectionId = 0x1005

ERROR_accounting_unknown_error = 0x0b05

ERROR_provisioning_auth_server_not_connected = 0x1110

ERROR_sound_could_not_open_playback_device = 0x0907

ERROR_voip_too_many_accounts = 0x1002

ERROR_ban_invalid_id = 0x0d00

ERROR_voip_pjsua = 0x1000

ERROR_file_invalid_name = 0x0800

ERROR_accounting_license_date_not_ok = 0x0b03

ERROR_server_invalid_id = 0x0400

ERROR_channel_maxclients_reached = 0x0309

ERROR_not_implemented = 0x0002

ERROR_database_no_modifications = 0x0503

ERROR_file_transfer_client_quota_exceeded = 0x0815

ERROR_failed_connection_initialisation = 0x0705

ERROR_command_not_found = 0x0100

ERROR_server_maxclients_reached = 0x0403

ERROR_sound_no_playback_device_available = 0x0905

ERROR_voip_cannot_answer_initiated_call = 0x1006

ERROR_provisioning_pool_unknown = 0x1104

ERROR_sound_device_busy = 0x0916

ERROR_vs_critical = 0x0700

ERROR_ok_no_update = 0x0003

ERROR_accounting_running_elsewhere = 0x0b0a

ERROR_channel_invalid_flags = 0x0307

ERROR_voip_internal_error = 0x1004

ERROR_sound_open_wave = 0x090d

ERROR_file_invalid_path = 0x0806

ERROR_whisper_no_targets = 0x070c

ERROR_accounting_slot_limit_reached = 0x0b01

ERROR_server_is_not_running = 0x0409

ERROR_file_transfer_complete = 0x0811

ERROR_ok = 0x0000

ERROR_client_too_many_clones_connected = 0x0209

ERROR_accounting_license_file_not_found = 0x0b02

ERROR_server_invalid_password = 0x0404

ERROR_channel_is_private_channel = 0x030e

ERROR_accounting_instance_check_error = 0x0b08

ERROR_client_hacked = 0x020d

ERROR_accounting_unable_to_connect_to_server = 0x0b04

ERROR_file_overwrite_excludes_resume = 0x0808

ERROR_accounting_instance_limit_reached = 0x0b07

ERROR_server_is_shutting_down = 0x0402

ERROR_lib_time_limit_reached = 0x0005

ERROR_provisioning_no_permission = 0x111A

ERROR_no_cached_connection_info = 0x0703

ERROR_file_invalid_size = 0x0809

ERROR_provisioning_not_connected = 0x1116

ERROR_sound_internal_encoder = 0x0902

ERROR_file_exceeds_supplied_size = 0x0810

ERROR_connect_failed_banned = 0x0d01

ERROR_permission_template_group_is_used = 0x0a0b

ERROR_sound_internal_preprocessor = 0x0901

ERROR_file_transfer_limit_reached = 0x0817

ERROR_file_transfer_connection_timeout = 0x080e

ERROR_parameter_not_found = 0x0603

ERROR_invalid_server_connection_handler_id = 0x0707

ERROR_parameter_missing = 0x0606

ERROR_file_invalid_permissions = 0x0801

ERROR_provisioning_already_connected = 0x1115

ERROR_provisioning_too_many_reserved = 0x1108

ERROR_server_is_booting = 0x040a

ERROR_privilege_key_invalid = 0x0f00

ERROR_server_unable_to_stop_own_server = 0x0406

ERROR_voip_already_initialized = 0x1001

ERROR_file_already_in_use = 0x080a

ERROR_client_invalid_id = 0x0200

ERROR_database_reinvoke = 0x0505

ERROR_provisioning_too_many_slots_requested = 0x1107

ERROR_tts_unable_to_initialize = 0x0e00

ERROR_provisioning_ts3server_not_found = 0x1119

ERROR_not_connected = 0x0702

ERROR_file_transfer_interrupted = 0x0813

ERROR_channel_no_filetransfer_supported = 0x030c

ERROR_server_version_outdated = 0x040d

ERROR_server_running = 0x0401

ERROR_message_invalid_id = 0x0c00

ERROR_sound_no_capture_device_available = 0x0904

ERROR_client_invalid_type = 0x0204

ERROR_accounting_virtualserver_limit_reached = 0x0b00

ERROR_sound_no_data = 0x0917

ERROR_provisioning_invalid_request = 0x1101

ERROR_parameter_invalid_size = 0x0605

ERROR_client_login_not_permitted = 0x020f

ERROR_sound_internal_capture = 0x090e

ERROR_permissions_group_not_empty = 0x0a07

ERROR_voip_invalid_account = 0x1003

ERROR_parameter_checksum = 0x0607

ERROR_channel_already_in = 0x0302

ERROR_whisper_too_many_targets = 0x070b

ERROR_channel_maxfamily_reached = 0x030a

ERROR_file_not_found = 0x0803

ERROR_client_protocol_limit_reached = 0x0203

ERROR_accounting_already_started = 0x0b0c

ERROR_voip_not_initialized = 0x1007

ERROR_parameter_invalid_count = 0x0601

ERROR_file_io_error = 0x0804

ERROR_permission_default_group_forbidden = 0x0a04

ERROR_provisioning_invalid_password = 0x1100

ERROR_database_empty_result = 0x0501

ERROR_could_not_resolve_hostname = 0x0706

ERROR_permissions = 0x0a0c

ERROR_client_nickname_inuse = 0x0201

ERROR_database_constraint = 0x0504

ERROR_provisioning_connecting = 0x1114

ERROR_permissions_client_insufficient = 0x0a08

ERROR_channel_invalid_id = 0x0300

ERROR_sound_unsupported_frequency = 0x0912

ERROR_sound_device_already_registerred = 0x0910

ERROR_permission_invalid_value = 0x0a06

ERROR_file_connection_lost = 0x080f

ERROR_provisioning_already_initialized = 0x1112

ERROR_ban_flooding = 0x0d03

ERROR_accounting_instance_duplicated = 0x0b0b

ERROR_channel_invalid_order = 0x030b

ERROR_channel_default_require_permanent = 0x0306

ERROR_provisioning_pool_missing = 0x1103

ERROR_permission_invalid_perm_id = 0x0a02

ERROR_accounting_not_started = 0x0b0d

ERROR_server_status_invalid = 0x040b

ERROR_rename_failed_banned = 0x0d02

ERROR_database = 0x0500

ERROR_client_is_flooding = 0x020c

ERROR_file_no_files_available = 0x0807

ERROR_channel_can_not_delete_default = 0x0305

ERROR_unable_to_bind_network_port = 0x0101

ERROR_sound_need_more_data = 0x0915

ERROR_database_duplicate_entry = 0x0502

ERROR_file_could_not_open_connection = 0x080b

ERROR_sound_unsupported_wave = 0x090c

ERROR_sound_invalid_channel_count = 0x0913

ERROR_file_transfer_canceled = 0x0812

ERROR_file_no_space_left_on_device = 0x080c

ERROR_sound_device_in_use = 0x090f

ERROR_client_not_subscribed = 0x0210

ERROR_channel_protocol_limit_reached = 0x0301

ERROR_currently_not_possible = 0x0704

ERROR_file_invalid_transfer_id = 0x0805

ERROR_connection_lost = 0x0701

ERROR_sound_internal_playback = 0x0903

ERROR_provisioning_auth_data_too_large = 0x1111

ERROR_channel_invalid_security_hash = 0x030f

ERROR_sound_unknown_device = 0x0911

ERROR_sound_preprocessor_disabled = 0x0900

ERROR_clientlibrary_not_initialised = 0x0709

ERROR_sound_channel_mask_mismatch = 0x0918

ERROR_could_not_initialise_input_manager = 0x0708

ERROR_client_is_online = 0x020b

ERROR_sound_could_not_open_capture_device = 0x0906

ERROR_undefined = 0x0001

ERROR_permissions_insufficient_group_power = 0x0a09

ERROR_file_exceeds_file_system_maximum_size = 0x080d

ERROR_accounting_server_error = 0x0b06

ERROR_channel_invalid_password = 0x030d

ERROR_provisioning_could_not_connect = 0x1109

ERROR_client_not_logged_in = 0x0206

ERROR_parameter_invalid = 0x0602

ERROR_permissions_insufficient_permission_power = 0x0a0a

ERROR_sound_invalid_playback_device = 0x090a

ERROR_sound_invalid_wave = 0x090b

ERROR_server_wrong_machineid = 0x0408

ERROR_channel_parent_not_permanent = 0x0308

ERROR_provisioning_invalid_timeout = 0x1118

ERROR_permission_empty_result = 0x0a03

ERROR_channel_not_empty = 0x0304

ERROR_client_version_outdated = 0x020a

ERROR_provisioning_io_error = 0x1117

ERROR_client_invalid_password = 0x0208


class Visibility(object):
    ENTER_VISIBILITY = 0
    RETAIN_VISIBILITY = 1
    LEAVE_VISIBILITY = 2
    
class ClientProperties(object):
    CLIENT_UNIQUE_IDENTIFIER = 0
    CLIENT_NICKNAME = 1
    CLIENT_VERSION = 2
    CLIENT_PLATFORM = 3
    CLIENT_FLAG_TALKING = 4
    CLIENT_INPUT_MUTED = 5
    CLIENT_OUTPUT_MUTED = 6
    CLIENT_OUTPUTONLY_MUTED = 7
    CLIENT_INPUT_HARDWARE = 8
    CLIENT_OUTPUT_HARDWARE = 9
    CLIENT_INPUT_DEACTIVATED = 10
    CLIENT_IDLE_TIME = 11
    CLIENT_DEFAULT_CHANNEL = 12
    CLIENT_DEFAULT_CHANNEL_PASSWORD = 13
    CLIENT_SERVER_PASSWORD = 14
    CLIENT_META_DATA = 15
    CLIENT_IS_MUTED = 16
    CLIENT_IS_RECORDING = 17
    CLIENT_VOLUME_MODIFICATOR = 18
    CLIENT_VERSION_SIGN = 19
    CLIENT_SECURITY_HASH = 20
    CLIENT_ENDMARKER = 21
    
class ServerInstancePropertiesRare(object):
    SERVERINSTANCE_DATABASE_VERSION = 0
    SERVERINSTANCE_FILETRANSFER_PORT = 1
    SERVERINSTANCE_SERVER_ENTROPY = 2
    SERVERINSTANCE_MONTHLY_TIMESTAMP = 3
    SERVERINSTANCE_MAX_DOWNLOAD_TOTAL_BANDWIDTH = 4
    SERVERINSTANCE_MAX_UPLOAD_TOTAL_BANDWIDTH = 5
    SERVERINSTANCE_GUEST_SERVERQUERY_GROUP = 6
    SERVERINSTANCE_SERVERQUERY_FLOOD_COMMANDS = 7
    SERVERINSTANCE_SERVERQUERY_FLOOD_TIME = 8
    SERVERINSTANCE_SERVERQUERY_BAN_TIME = 9
    SERVERINSTANCE_TEMPLATE_SERVERADMIN_GROUP = 10
    SERVERINSTANCE_TEMPLATE_SERVERDEFAULT_GROUP = 11
    SERVERINSTANCE_TEMPLATE_CHANNELADMIN_GROUP = 12
    SERVERINSTANCE_TEMPLATE_CHANNELDEFAULT_GROUP = 13
    SERVERINSTANCE_PERMISSIONS_VERSION = 14
    SERVERINSTANCE_PENDING_CONNECTIONS_PER_IP = 15
    SERVERINSTANCE_ENDMARKER_RARE = 16
    
class LogLevel(object):
    LogLevel_CRITICAL = 0
    LogLevel_ERROR = 1
    LogLevel_WARNING = 2
    LogLevel_DEBUG = 3
    LogLevel_INFO = 4
    LogLevel_DEVEL = 5
    
class ReasonIdentifier(object):
    REASON_NONE = 0
    REASON_MOVED = 1
    REASON_SUBSCRIPTION = 2
    REASON_LOST_CONNECTION = 3
    REASON_KICK_CHANNEL = 4
    REASON_KICK_SERVER = 5
    REASON_KICK_SERVER_BAN = 6
    REASON_SERVERSTOP = 7
    REASON_CLIENTDISCONNECT = 8
    REASON_CHANNELUPDATE = 9
    REASON_CHANNELEDIT = 10
    REASON_CLIENTDISCONNECT_SERVER_SHUTDOWN = 11
    
class SecuritySaltOptions(object):
    SECURITY_SALT_CHECK_NICKNAME = 1
    SECURITY_SALT_CHECK_META_DATA = 2
    
class ChannelProperties(object):
    CHANNEL_NAME = 0
    CHANNEL_TOPIC = 1
    CHANNEL_DESCRIPTION = 2
    CHANNEL_PASSWORD = 3
    CHANNEL_CODEC = 4
    CHANNEL_CODEC_QUALITY = 5
    CHANNEL_MAXCLIENTS = 6
    CHANNEL_MAXFAMILYCLIENTS = 7
    CHANNEL_ORDER = 8
    CHANNEL_FLAG_PERMANENT = 9
    CHANNEL_FLAG_SEMI_PERMANENT = 10
    CHANNEL_FLAG_DEFAULT = 11
    CHANNEL_FLAG_PASSWORD = 12
    CHANNEL_CODEC_LATENCY_FACTOR = 13
    CHANNEL_CODEC_IS_UNENCRYPTED = 14
    CHANNEL_SECURITY_SALT = 15
    CHANNEL_DELETE_DELAY = 16
    CHANNEL_ENDMARKER = 17
    
class ConnectStatus(object):
    STATUS_DISCONNECTED = 0
    STATUS_CONNECTING = 1
    STATUS_CONNECTED = 2
    STATUS_CONNECTION_ESTABLISHING = 3
    STATUS_CONNECTION_ESTABLISHED = 4
    
class TextMessageTargetMode(object):
    TextMessageTarget_CLIENT = 1
    TextMessageTarget_CHANNEL = 2
    TextMessageTarget_SERVER = 3
    TextMessageTarget_MAX = 4
    
class PluginGuiProfile(object):
    PLUGIN_GUI_SOUND_CAPTURE = 0
    PLUGIN_GUI_SOUND_PLAYBACK = 1
    PLUGIN_GUI_HOTKEY = 2
    PLUGIN_GUI_SOUNDPACK = 3
    PLUGIN_GUI_IDENTITY = 4
    
class CommandLinePropertiesRare(object):
    COMMANDLINE_NOTHING = 0
    COMMANDLINE_ENDMARKER_RARE = 1
    
class GroupWhisperType(object):
    GROUPWHISPERTYPE_SERVERGROUP = 0
    GROUPWHISPERTYPE_CHANNELGROUP = 1
    GROUPWHISPERTYPE_CHANNELCOMMANDER = 2
    GROUPWHISPERTYPE_ALLCLIENTS = 3
    GROUPWHISPERTYPE_ENDMARKER = 4
    
class LicenseViolationType(object):
    NO_VIOLATION = 0
    SLOT_VIOLATION = 1
    SLOT_SUSPICION = 2
    
class PluginConnectTab(object):
    PLUGIN_CONNECT_TAB_NEW = 0
    PLUGIN_CONNECT_TAB_CURRENT = 1
    PLUGIN_CONNECT_TAB_NEW_IF_CURRENT_CONNECTED = 2
    
class HostMessageMode(object):
    HostMessageMode_NONE = 0
    HostMessageMode_LOG = 1
    HostMessageMode_MODAL = 2
    HostMessageMode_MODALQUIT = 3
    
class ConnectionPropertiesRare(object):
    CONNECTION_DUMMY_0 = 52
    CONNECTION_DUMMY_1 = 53
    CONNECTION_DUMMY_2 = 54
    CONNECTION_DUMMY_3 = 55
    CONNECTION_DUMMY_4 = 56
    CONNECTION_DUMMY_5 = 57
    CONNECTION_DUMMY_6 = 58
    CONNECTION_DUMMY_7 = 59
    CONNECTION_DUMMY_8 = 60
    CONNECTION_DUMMY_9 = 61
    CONNECTION_FILETRANSFER_BANDWIDTH_SENT = 62
    CONNECTION_FILETRANSFER_BANDWIDTH_RECEIVED = 63
    CONNECTION_FILETRANSFER_BYTES_RECEIVED_TOTAL = 64
    CONNECTION_FILETRANSFER_BYTES_SENT_TOTAL = 65
    CONNECTION_ENDMARKER_RARE = 66
    
class HardwareOutputStatus(object):
    HARDWAREOUTPUT_DISABLED = 0
    HARDWAREOUTPUT_ENABLED = 1
    
class InputDeactivationStatus(object):
    INPUT_ACTIVE = 0
    INPUT_DEACTIVATED = 1
    
class ACLType(object):
    ACL_NONE = 0
    ACL_WHITE_LIST = 1
    ACL_BLACK_LIST = 2
    
class CodecEncryptionMode(object):
    CODEC_ENCRYPTION_PER_CHANNEL = 0
    CODEC_ENCRYPTION_FORCED_OFF = 1
    CODEC_ENCRYPTION_FORCED_ON = 2
    
class VirtualServerPropertiesRare(object):
    VIRTUALSERVER_DUMMY_0 = 12
    VIRTUALSERVER_DUMMY_1 = 13
    VIRTUALSERVER_DUMMY_2 = 14
    VIRTUALSERVER_DUMMY_3 = 15
    VIRTUALSERVER_DUMMY_4 = 16
    VIRTUALSERVER_DUMMY_5 = 17
    VIRTUALSERVER_DUMMY_6 = 18
    VIRTUALSERVER_DUMMY_7 = 19
    VIRTUALSERVER_DUMMY_8 = 20
    VIRTUALSERVER_KEYPAIR = 21
    VIRTUALSERVER_HOSTMESSAGE = 22
    VIRTUALSERVER_HOSTMESSAGE_MODE = 23
    VIRTUALSERVER_FILEBASE = 24
    VIRTUALSERVER_DEFAULT_SERVER_GROUP = 25
    VIRTUALSERVER_DEFAULT_CHANNEL_GROUP = 26
    VIRTUALSERVER_FLAG_PASSWORD = 27
    VIRTUALSERVER_DEFAULT_CHANNEL_ADMIN_GROUP = 28
    VIRTUALSERVER_MAX_DOWNLOAD_TOTAL_BANDWIDTH = 29
    VIRTUALSERVER_MAX_UPLOAD_TOTAL_BANDWIDTH = 30
    VIRTUALSERVER_HOSTBANNER_URL = 31
    VIRTUALSERVER_HOSTBANNER_GFX_URL = 32
    VIRTUALSERVER_HOSTBANNER_GFX_INTERVAL = 33
    VIRTUALSERVER_COMPLAIN_AUTOBAN_COUNT = 34
    VIRTUALSERVER_COMPLAIN_AUTOBAN_TIME = 35
    VIRTUALSERVER_COMPLAIN_REMOVE_TIME = 36
    VIRTUALSERVER_MIN_CLIENTS_IN_CHANNEL_BEFORE_FORCED_SILENCE = 37
    VIRTUALSERVER_PRIORITY_SPEAKER_DIMM_MODIFICATOR = 38
    VIRTUALSERVER_ID = 39
    VIRTUALSERVER_ANTIFLOOD_POINTS_TICK_REDUCE = 40
    VIRTUALSERVER_ANTIFLOOD_POINTS_NEEDED_COMMAND_BLOCK = 41
    VIRTUALSERVER_ANTIFLOOD_POINTS_NEEDED_IP_BLOCK = 42
    VIRTUALSERVER_CLIENT_CONNECTIONS = 43
    VIRTUALSERVER_QUERY_CLIENT_CONNECTIONS = 44
    VIRTUALSERVER_HOSTBUTTON_TOOLTIP = 45
    VIRTUALSERVER_HOSTBUTTON_URL = 46
    VIRTUALSERVER_HOSTBUTTON_GFX_URL = 47
    VIRTUALSERVER_QUERYCLIENTS_ONLINE = 48
    VIRTUALSERVER_DOWNLOAD_QUOTA = 49
    VIRTUALSERVER_UPLOAD_QUOTA = 50
    VIRTUALSERVER_MONTH_BYTES_DOWNLOADED = 51
    VIRTUALSERVER_MONTH_BYTES_UPLOADED = 52
    VIRTUALSERVER_TOTAL_BYTES_DOWNLOADED = 53
    VIRTUALSERVER_TOTAL_BYTES_UPLOADED = 54
    VIRTUALSERVER_PORT = 55
    VIRTUALSERVER_AUTOSTART = 56
    VIRTUALSERVER_MACHINE_ID = 57
    VIRTUALSERVER_NEEDED_IDENTITY_SECURITY_LEVEL = 58
    VIRTUALSERVER_LOG_CLIENT = 59
    VIRTUALSERVER_LOG_QUERY = 60
    VIRTUALSERVER_LOG_CHANNEL = 61
    VIRTUALSERVER_LOG_PERMISSIONS = 62
    VIRTUALSERVER_LOG_SERVER = 63
    VIRTUALSERVER_LOG_FILETRANSFER = 64
    VIRTUALSERVER_MIN_CLIENT_VERSION = 65
    VIRTUALSERVER_NAME_PHONETIC = 66
    VIRTUALSERVER_ICON_ID = 67
    VIRTUALSERVER_RESERVED_SLOTS = 68
    VIRTUALSERVER_TOTAL_PACKETLOSS_SPEECH = 69
    VIRTUALSERVER_TOTAL_PACKETLOSS_KEEPALIVE = 70
    VIRTUALSERVER_TOTAL_PACKETLOSS_CONTROL = 71
    VIRTUALSERVER_TOTAL_PACKETLOSS_TOTAL = 72
    VIRTUALSERVER_TOTAL_PING = 73
    VIRTUALSERVER_IP = 74
    VIRTUALSERVER_WEBLIST_ENABLED = 75
    VIRTUALSERVER_AUTOGENERATED_PRIVILEGEKEY = 76
    VIRTUALSERVER_ASK_FOR_PRIVILEGEKEY = 77
    VIRTUALSERVER_HOSTBANNER_MODE = 78
    VIRTUALSERVER_CHANNEL_TEMP_DELETE_DELAY_DEFAULT = 79
    VIRTUALSERVER_MIN_ANDROID_VERSION = 80
    VIRTUALSERVER_MIN_IOS_VERSION = 81
    VIRTUALSERVER_MIN_WINPHONE_VERSION = 82
    VIRTUALSERVER_ENDMARKER_RARE = 83
    
class PluginItemType(object):
    PLUGIN_SERVER = 0
    PLUGIN_CHANNEL = 1
    PLUGIN_CLIENT = 2
    
class GroupWhisperTargetMode(object):
    GROUPWHISPERTARGETMODE_ALL = 0
    GROUPWHISPERTARGETMODE_CURRENTCHANNEL = 1
    GROUPWHISPERTARGETMODE_PARENTCHANNEL = 2
    GROUPWHISPERTARGETMODE_ALLPARENTCHANNELS = 3
    GROUPWHISPERTARGETMODE_CHANNELFAMILY = 4
    GROUPWHISPERTARGETMODE_ANCESTORCHANNELFAMILY = 5
    GROUPWHISPERTARGETMODE_SUBCHANNELS = 6
    GROUPWHISPERTARGETMODE_ENDMARKER = 7
    
class PluginConfigureOffer(object):
    PLUGIN_OFFERS_NO_CONFIGURE = 0
    PLUGIN_OFFERS_CONFIGURE_NEW_THREAD = 1
    PLUGIN_OFFERS_CONFIGURE_QT_THREAD = 2
    
class MuteOutputStatus(object):
    MUTEOUTPUT_NONE = 0
    MUTEOUTPUT_MUTED = 1
    
class HardwareInputStatus(object):
    HARDWAREINPUT_DISABLED = 0
    HARDWAREINPUT_ENABLED = 1
    
class ClientPropertiesRare(object):
    CLIENT_DUMMY_3 = 21
    CLIENT_DUMMY_4 = 22
    CLIENT_DUMMY_5 = 23
    CLIENT_DUMMY_6 = 24
    CLIENT_DUMMY_7 = 25
    CLIENT_DUMMY_8 = 26
    CLIENT_DUMMY_9 = 27
    CLIENT_KEY_OFFSET = 28
    CLIENT_LAST_VAR_REQUEST = 29
    CLIENT_LOGIN_NAME = 30
    CLIENT_LOGIN_PASSWORD = 31
    CLIENT_DATABASE_ID = 32
    CLIENT_CHANNEL_GROUP_ID = 33
    CLIENT_SERVERGROUPS = 34
    CLIENT_CREATED = 35
    CLIENT_LASTCONNECTED = 36
    CLIENT_TOTALCONNECTIONS = 37
    CLIENT_AWAY = 38
    CLIENT_AWAY_MESSAGE = 39
    CLIENT_TYPE = 40
    CLIENT_FLAG_AVATAR = 41
    CLIENT_TALK_POWER = 42
    CLIENT_TALK_REQUEST = 43
    CLIENT_TALK_REQUEST_MSG = 44
    CLIENT_DESCRIPTION = 45
    CLIENT_IS_TALKER = 46
    CLIENT_MONTH_BYTES_UPLOADED = 47
    CLIENT_MONTH_BYTES_DOWNLOADED = 48
    CLIENT_TOTAL_BYTES_UPLOADED = 49
    CLIENT_TOTAL_BYTES_DOWNLOADED = 50
    CLIENT_IS_PRIORITY_SPEAKER = 51
    CLIENT_UNREAD_MESSAGES = 52
    CLIENT_NICKNAME_PHONETIC = 53
    CLIENT_NEEDED_SERVERQUERY_VIEW_POWER = 54
    CLIENT_DEFAULT_TOKEN = 55
    CLIENT_ICON_ID = 56
    CLIENT_IS_CHANNEL_COMMANDER = 57
    CLIENT_COUNTRY = 58
    CLIENT_CHANNEL_GROUP_INHERITED_CHANNEL_ID = 59
    CLIENT_BADGES = 60
    CLIENT_ENDMARKER_RARE = 61
    
class PluginTargetMode(object):
    PluginCommandTarget_CURRENT_CHANNEL = 0
    PluginCommandTarget_SERVER = 1
    PluginCommandTarget_CLIENT = 2
    PluginCommandTarget_CURRENT_CHANNEL_SUBSCRIBED_CLIENTS = 3
    PluginCommandTarget_MAX = 4
    
class PluginMessageTarget(object):
    PLUGIN_MESSAGE_TARGET_SERVER = 0
    PLUGIN_MESSAGE_TARGET_CHANNEL = 1
    
class AwayStatus(object):
    AWAY_NONE = 0
    AWAY_ZZZ = 1
    
class ChannelPropertiesRare(object):
    CHANNEL_DUMMY_2 = 17
    CHANNEL_DUMMY_3 = 18
    CHANNEL_DUMMY_4 = 19
    CHANNEL_DUMMY_5 = 20
    CHANNEL_DUMMY_6 = 21
    CHANNEL_DUMMY_7 = 22
    CHANNEL_FLAG_MAXCLIENTS_UNLIMITED = 23
    CHANNEL_FLAG_MAXFAMILYCLIENTS_UNLIMITED = 24
    CHANNEL_FLAG_MAXFAMILYCLIENTS_INHERITED = 25
    CHANNEL_FLAG_ARE_SUBSCRIBED = 26
    CHANNEL_FILEPATH = 27
    CHANNEL_NEEDED_TALK_POWER = 28
    CHANNEL_FORCED_SILENCE = 29
    CHANNEL_NAME_PHONETIC = 30
    CHANNEL_ICON_ID = 31
    CHANNEL_FLAG_PRIVATE = 32
    CHANNEL_ENDMARKER_RARE = 33
    
class FileListType(object):
    FileListType_Directory = 0
    FileListType_File = 1
    
class TalkStatus(object):
    STATUS_NOT_TALKING = 0
    STATUS_TALKING = 1
    STATUS_TALKING_WHILE_DISABLED = 2
    
class SERVER_BINDING(object):
    SERVER_BINDING_VIRTUALSERVER = 0
    SERVER_BINDING_SERVERQUERY = 1
    SERVER_BINDING_FILETRANSFER = 2
    
class FTAction(object):
    FT_INIT_SERVER = 0
    FT_INIT_CHANNEL = 1
    FT_UPLOAD = 2
    FT_DOWNLOAD = 3
    FT_DELETE = 4
    FT_CREATEDIR = 5
    FT_RENAME = 6
    FT_FILELIST = 7
    FT_FILEINFO = 8
    
class MonoSoundDestination(object):
    MONO_SOUND_DESTINATION_ALL = 0
    MONO_SOUND_DESTINATION_FRONT_CENTER = 1
    MONO_SOUND_DESTINATION_FRONT_LEFT_AND_RIGHT = 2
    
class ConnectionProperties(object):
    CONNECTION_PING = 0
    CONNECTION_PING_DEVIATION = 1
    CONNECTION_CONNECTED_TIME = 2
    CONNECTION_IDLE_TIME = 3
    CONNECTION_CLIENT_IP = 4
    CONNECTION_CLIENT_PORT = 5
    CONNECTION_SERVER_IP = 6
    CONNECTION_SERVER_PORT = 7
    CONNECTION_PACKETS_SENT_SPEECH = 8
    CONNECTION_PACKETS_SENT_KEEPALIVE = 9
    CONNECTION_PACKETS_SENT_CONTROL = 10
    CONNECTION_PACKETS_SENT_TOTAL = 11
    CONNECTION_BYTES_SENT_SPEECH = 12
    CONNECTION_BYTES_SENT_KEEPALIVE = 13
    CONNECTION_BYTES_SENT_CONTROL = 14
    CONNECTION_BYTES_SENT_TOTAL = 15
    CONNECTION_PACKETS_RECEIVED_SPEECH = 16
    CONNECTION_PACKETS_RECEIVED_KEEPALIVE = 17
    CONNECTION_PACKETS_RECEIVED_CONTROL = 18
    CONNECTION_PACKETS_RECEIVED_TOTAL = 19
    CONNECTION_BYTES_RECEIVED_SPEECH = 20
    CONNECTION_BYTES_RECEIVED_KEEPALIVE = 21
    CONNECTION_BYTES_RECEIVED_CONTROL = 22
    CONNECTION_BYTES_RECEIVED_TOTAL = 23
    CONNECTION_PACKETLOSS_SPEECH = 24
    CONNECTION_PACKETLOSS_KEEPALIVE = 25
    CONNECTION_PACKETLOSS_CONTROL = 26
    CONNECTION_PACKETLOSS_TOTAL = 27
    CONNECTION_SERVER2CLIENT_PACKETLOSS_SPEECH = 28
    CONNECTION_SERVER2CLIENT_PACKETLOSS_KEEPALIVE = 29
    CONNECTION_SERVER2CLIENT_PACKETLOSS_CONTROL = 30
    CONNECTION_SERVER2CLIENT_PACKETLOSS_TOTAL = 31
    CONNECTION_CLIENT2SERVER_PACKETLOSS_SPEECH = 32
    CONNECTION_CLIENT2SERVER_PACKETLOSS_KEEPALIVE = 33
    CONNECTION_CLIENT2SERVER_PACKETLOSS_CONTROL = 34
    CONNECTION_CLIENT2SERVER_PACKETLOSS_TOTAL = 35
    CONNECTION_BANDWIDTH_SENT_LAST_SECOND_SPEECH = 36
    CONNECTION_BANDWIDTH_SENT_LAST_SECOND_KEEPALIVE = 37
    CONNECTION_BANDWIDTH_SENT_LAST_SECOND_CONTROL = 38
    CONNECTION_BANDWIDTH_SENT_LAST_SECOND_TOTAL = 39
    CONNECTION_BANDWIDTH_SENT_LAST_MINUTE_SPEECH = 40
    CONNECTION_BANDWIDTH_SENT_LAST_MINUTE_KEEPALIVE = 41
    CONNECTION_BANDWIDTH_SENT_LAST_MINUTE_CONTROL = 42
    CONNECTION_BANDWIDTH_SENT_LAST_MINUTE_TOTAL = 43
    CONNECTION_BANDWIDTH_RECEIVED_LAST_SECOND_SPEECH = 44
    CONNECTION_BANDWIDTH_RECEIVED_LAST_SECOND_KEEPALIVE = 45
    CONNECTION_BANDWIDTH_RECEIVED_LAST_SECOND_CONTROL = 46
    CONNECTION_BANDWIDTH_RECEIVED_LAST_SECOND_TOTAL = 47
    CONNECTION_BANDWIDTH_RECEIVED_LAST_MINUTE_SPEECH = 48
    CONNECTION_BANDWIDTH_RECEIVED_LAST_MINUTE_KEEPALIVE = 49
    CONNECTION_BANDWIDTH_RECEIVED_LAST_MINUTE_CONTROL = 50
    CONNECTION_BANDWIDTH_RECEIVED_LAST_MINUTE_TOTAL = 51
    CONNECTION_ENDMARKER = 52
    
class FileTransferState(object):
    FILETRANSFER_INITIALISING = 0
    FILETRANSFER_ACTIVE = 1
    FILETRANSFER_FINISHED = 2
    
class ClientType(object):
    ClientType_NORMAL = 0
    ClientType_SERVERQUERY = 1
    
class GroupShowNameTreeMode(object):
    GroupShowNameTreeMode_NONE = 0
    GroupShowNameTreeMode_BEFORE = 1
    GroupShowNameTreeMode_BEHIND = 2
    
class CodecType(object):
    CODEC_SPEEX_NARROWBAND = 0
    CODEC_SPEEX_WIDEBAND = 1
    CODEC_SPEEX_ULTRAWIDEBAND = 2
    CODEC_CELT_MONO = 3
    CODEC_OPUS_VOICE = 4
    CODEC_OPUS_MUSIC = 5
    
class BBCodeTags(object):
    BBCodeTag_B = 0x00000001
    BBCodeTag_I = 0x00000002
    BBCodeTag_U = 0x00000004
    BBCodeTag_S = 0x00000008
    BBCodeTag_SUP = 0x00000010
    BBCodeTag_SUB = 0x00000020
    BBCodeTag_COLOR = 0x00000040
    BBCodeTag_SIZE = 0x00000080
    BBCodeTag_group_text = 0x000000FF
    BBCodeTag_LEFT = 0x00001000
    BBCodeTag_RIGHT = 0x00002000
    BBCodeTag_CENTER = 0x00004000
    BBCodeTag_group_align = 0x00007000
    BBCodeTag_URL = 0x00010000
    BBCodeTag_IMAGE = 0x00020000
    BBCodeTag_HR = 0x00040000
    BBCodeTag_LIST = 0x00100000
    BBCodeTag_LISTITEM = 0x00200000
    BBCodeTag_group_list = 0x00300000
    BBCodeTag_TABLE = 0x00400000
    BBCodeTag_TR = 0x00800000
    BBCodeTag_TH = 0x01000000
    BBCodeTag_TD = 0x02000000
    BBCodeTag_group_table = 0x03C00000
    BBCodeTag_def_simple = ((((((BBCodeTag_B | BBCodeTag_I) | BBCodeTag_U) | BBCodeTag_S) | BBCodeTag_SUP) | BBCodeTag_SUB) | BBCodeTag_COLOR) | BBCodeTag_URL
    BBCodeTag_def_simple_Img = BBCodeTag_def_simple | BBCodeTag_IMAGE
    BBCodeTag_def_extended = (((((BBCodeTag_group_text | BBCodeTag_group_align) | BBCodeTag_URL) | BBCodeTag_IMAGE) | BBCodeTag_HR) | BBCodeTag_group_list) | BBCodeTag_group_table
    
class PluginMenuType(object):
    PLUGIN_MENU_TYPE_GLOBAL = 0
    PLUGIN_MENU_TYPE_CHANNEL = 1
    PLUGIN_MENU_TYPE_CLIENT = 2
    
class VirtualServerProperties(object):
    VIRTUALSERVER_UNIQUE_IDENTIFIER = 0
    VIRTUALSERVER_NAME = 1
    VIRTUALSERVER_WELCOMEMESSAGE = 2
    VIRTUALSERVER_PLATFORM = 3
    VIRTUALSERVER_VERSION = 4
    VIRTUALSERVER_MAXCLIENTS = 5
    VIRTUALSERVER_PASSWORD = 6
    VIRTUALSERVER_CLIENTS_ONLINE = 7
    VIRTUALSERVER_CHANNELS_ONLINE = 8
    VIRTUALSERVER_CREATED = 9
    VIRTUALSERVER_UPTIME = 10
    VIRTUALSERVER_CODEC_ENCRYPTION_MODE = 11
    VIRTUALSERVER_ENDMARKER = 12
    
class LocalTestMode(object):
    TEST_MODE_OFF = 0
    TEST_MODE_VOICE_LOCAL_ONLY = 1
    TEST_MODE_VOICE_LOCAL_AND_REMOTE = 2
    
class HostBannerMode(object):
    HostBannerMode_NO_ADJUST = 0
    HostBannerMode_ADJUST_IGNORE_ASPECT = 1
    HostBannerMode_ADJUST_KEEP_ASPECT = 2
    
class ClientCommand(object):
    CLIENT_COMMAND_requestConnectionInfo = 0
    CLIENT_COMMAND_requestClientMove = 1
    CLIENT_COMMAND_requestXXMuteClients = 2
    CLIENT_COMMAND_requestClientKickFromXXX = 3
    CLIENT_COMMAND_flushChannelCreation = 4
    CLIENT_COMMAND_flushChannelUpdates = 5
    CLIENT_COMMAND_requestChannelMove = 6
    CLIENT_COMMAND_requestChannelDelete = 7
    CLIENT_COMMAND_requestChannelDescription = 8
    CLIENT_COMMAND_requestChannelXXSubscribeXXX = 9
    CLIENT_COMMAND_requestServerConnectionInfo = 10
    CLIENT_COMMAND_requestSendXXXTextMsg = 11
    CLIENT_COMMAND_filetransfers = 12
    CLIENT_COMMAND_ENDMARKER = 13
    
class MuteInputStatus(object):
    MUTEINPUT_NONE = 0
    MUTEINPUT_MUTED = 1
    
class LogTypes(object):
    LogType_NONE = 0x0000
    LogType_FILE = 0x0001
    LogType_CONSOLE = 0x0002
    LogType_USERLOGGING = 0x0004
    LogType_NO_NETLOGGING = 0x0008
    LogType_DATABASE = 0x0010
    LogType_SYSLOG = 0x0020
    