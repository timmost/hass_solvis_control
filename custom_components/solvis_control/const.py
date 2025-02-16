from dataclasses import dataclass
from enum import IntEnum

DOMAIN = "solvis_control"

CONF_NAME = "name"
CONF_HOST = "host"
CONF_PORT = "port"

DEVICE_VERSION = "device_version"
POLL_RATE_DEFAULT = "poll_rate_default"
POLL_RATE_SLOW = "poll_rate_slow"

# Option attributes to make certain values configurable
CONF_OPTION_1 = "HKR2"  # HKR 2
CONF_OPTION_2 = "HKR3"  # HKR 3
CONF_OPTION_3 = "solar collector"  # Solar collector
CONF_OPTION_4 = "heat pump"  # heat pump

DATA_COORDINATOR = "coordinator"
MANUFACTURER = "Solvis"
PORT = 502


class SolvisDeviceVersion(IntEnum):
	"""Enum for device versions."""

	SC2 = 2
	SC3 = 1


@dataclass
class ModbusFieldConfig:
	name: str
	address: int
	unit: str | None
	device_class: str | None
	state_class: str | None
	multiplier: float = 0.1
	absolute_value: bool = False

	register: int = 1
	# 1 = INPUT, 2 = HOLDING

	entity_category: str = None

	enabled_by_default: bool = True
	# Option to disable entitiy by default

	edit: bool = False
	# Allows entities to be set to editable

	range_data: tuple = None
	# Assigns a range for number entities input_type = 2

	step_size: float = None

	options: tuple = None
	# Assigns possible potions for select entities input_type = 1

	conf_option: int = 0
	# Assign CONF_OPTION to entities

	input_type: int = 0
	# Configuration for which state class a register belongs to
	# Possibilities:
	# sensor (0), select (1), number (2), switch (3), binary_sensor (4)

	data_processing: int = 0
	# Option to further process data
	# 0: no processing, 1: version string split, 2: special conversion

	supported_version: int = 0
	# Supported Version
	# 0: SC2 & SC3, 1: SC3, 2: SC2

	poll_rate: bool = False
	# False: default, True: slow

	poll_time: int = 0
	# Internal variable to store the value of the last poll
	# Don't change

	byte_swap: int = 0
	# endianness (byte_order)
	# 0: big endian (default), 1: little endian

	suggested_precision: int | None = 1


# Naming Scheme
# [heating_circuit]_[parameter]_[solvis_name]
# Example: hkr1_flow_water_temp_s12
REGISTERS = [
	ModbusFieldConfig(  # Analog Out 1 Status
		name="gas_burner_modulation_O1",
		address=3840,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
	),
	ModbusFieldConfig(  # Analog Out 2 Status
		name="solar_pump_primary_O2",
		address=3845,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
		conf_option=3
	),
	ModbusFieldConfig(  # Analog Out 3 Status
		name="solar_pump_secondary_O3",
		address=3850,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
		conf_option=3
	),
	ModbusFieldConfig(  # Analog Out 4 Status
		name="heatpump_charging_pump_O4",
		address=3855,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
		conf_option=4,
	),
	ModbusFieldConfig(  # Analog Out 5 Status
		name="heatpump_O5",
		address=3860,
		enabled_by_default=False,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
		conf_option=4,
	),
	ModbusFieldConfig(  # Analog Out 6 Status
		name="analog_out_6_status_O6",
		address=3865,
		enabled_by_default=False,
		device_class=None,
		unit=None,
		state_class="measurement",
		entity_category="diagnostic",
		poll_time=0,
	),
	ModbusFieldConfig(  # Wärmeerzeuger SX aktuelle Leistung
		name="waermeerzeuger_leistung_SX",
		address=33539,
		unit="kW",
		device_class="power",
		state_class="measurement",
		poll_time=0,
	),
	# ModbusFieldConfig(  # TODO: check
	# 	name="laufzeit_brennerstufe_1",
	# 	address=33536,
	# 	enabled_by_default=False,
	# 	device_class="duration",
	# 	unit="h",
	# 	state_class="measurement",
	# 	poll_time=0,
	# ),
	# ModbusFieldConfig(  # TODO: check
	# 	name="laufzeit_brennerstufe_2",
	# 	address=33538,
	# 	enabled_by_default=False,
	# 	device_class="duration",
	# 	unit="h",
	# 	state_class="measurement",
	# 	poll_time=0,
	# ),
	ModbusFieldConfig(  # Außentemperatur
		name="outdoor_air_temp_s10",
		address=33033,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(
		name="temperatur_solar_collector_S8",
		address=33031,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		conf_option=3,
		poll_time=0,
	),
	ModbusFieldConfig(  # Zirkulationsdurchfluss
		name="temperatur_circulation_S11",
		address=33034,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		multiplier=0.1,
		poll_time=0,
	),
	ModbusFieldConfig(  # Vorlauftemperatur HKR1
		name="hkr1_flow_water_temp_S12",
		address=33035,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(  # Vorlauftemperatur HKR2
		name="hkr2_flow_water_temp_S13",
		address=33036,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		conf_option=1,
		poll_time=0,
	),
	ModbusFieldConfig(  # Vorlauftemperatur HKR3
		name="hkr3_flow_water_temp_S14",
		address=33039,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		enabled_by_default=False,
		conf_option=2,
		poll_time=0,
	),
	ModbusFieldConfig(  # Warmwassertemperatur
		name="domestic_water_temp_S2",
		address=33025,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(  # Warmwasser Nachheizung
		name="domestic_water_reheat",
		address=2322,
		unit=None,
		device_class=None,
		state_class="measurement",
		multiplier=1,
		input_type=3,
		register=2,
		poll_time=0,
	),
	ModbusFieldConfig(
		name="temperature_solar_flow_primary_S7",
		address=33030,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		conf_option=3,
		poll_time=0,
	),
	ModbusFieldConfig(
		name="temperature_solar_return_secondary_S6",
		address=33029,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		conf_option=3,
		poll_time=0,
	),
	ModbusFieldConfig(
		name="temperature_solar_flow_secondary_S5",
		address=33028,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		conf_option=3,
		poll_time=0,
	),
	ModbusFieldConfig(  # Speicherreferenztemperatur
		name="temperature_storage_reference_S3",
		address=33026,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(  # Heizungspuffertemperatur unten
		name="temperature_heating_buffer_lower_S9",
		address=33032,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		absolute_value=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Heizungspuffertemperatur oben
		name="temperature_heating_buffer_upper_S4",
		address=33027,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		absolute_value=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Warmwasserpuffer
		name="temperature_storage_top_S1",
		address=33024,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(  # Kaltwassertemperatur
		name="temperatur_cold_water_S15",
		address=33038,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		poll_time=0,
	),
	ModbusFieldConfig(  # Brennerstarts
		name="number_gas_burner_start",
		address=33537,
		unit=None,
		device_class=None,
		state_class="measurement",
		multiplier=1,
		entity_category="diagnostic",
		absolute_value=True,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Ionisationsstrom
		name="ionisation_current",
		address=33540,
		unit="mA",
		device_class="current",
		state_class="measurement",
		poll_time=0,
		multiplier=0.0000001,
	),
	ModbusFieldConfig(  # A01 Pumpe Zirkulation
		name="circulation_pump_A1",
		address=33280,
		unit="%",
		device_class=None,
		state_class="measurement",
		multiplier=1.0,
		byte_swap=1,
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # A02 Pumpe Warmwasser
		name="hot_water_pump_A2",
		address=33281,
		unit="%",
		device_class=None,
		state_class="measurement",
		multiplier=1.0,
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # A03 Pumpe HKR 1
		name="hkr1_pump_A3",
		address=33282,
		unit="%",
		device_class=None,
		state_class="measurement",
		multiplier=1.0,
		byte_swap=1,
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # A04 Pumpe HKR 2
		name="hkr2_pump_A4",
		address=33283,
		unit="%",
		device_class=None,
		state_class="measurement",
		multiplier=1.0,
		byte_swap=1,
		conf_option=1,
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # A05 Pumpe HKR 3
		name="hkr3_pump_A5",
		address=33284,
		unit="%",
		device_class=None,
		state_class="measurement",
		multiplier=1.0,
		byte_swap=1,
		conf_option=2,
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # A12 Brennerstatus
		name="burner_status_A12",  # maybe also valve for remote heat, depending on config
		address=33291,
		unit="%",
		multiplier=1,
		byte_swap=1,
		device_class=None,
		state_class="measurement",
		poll_time=0,
		input_type=4,
		supported_version=1,
	),
	ModbusFieldConfig(  # A12 Brennerstatus
		name="burner_status_A12",  # maybe also valve for remote heat, depending on config
		address=33291,
		unit="%",
		multiplier=1,
		device_class=None,
		state_class="measurement",
		poll_time=0,
		input_type=4,
		supported_version=2,
	),
	ModbusFieldConfig(  # S17
		name="solar_volume_flow_s17",
		address=33040,
		unit="l/h",
		device_class=None,
		state_class="measurement",
		multiplier=1,
		conf_option=3,
		poll_time=0,
		supported_version=1,  # SC3
	),
	ModbusFieldConfig(  # S17
		name="solar_volume_flow_s17",
		address=33040,
		unit="l/min",
		device_class=None,
		state_class="measurement",
		multiplier=1,
		conf_option=3,
		poll_time=0,
		data_processing=3,
		supported_version=2,  # SC2
	),
	ModbusFieldConfig(  # Solarleistung
		name="solar_power",
		address=33543,
		unit="kW",
		device_class="power",
		state_class="measurement",
		register=2,
		edit=False,
		conf_option=3,
		poll_time=0,
		supported_version=1,
	),
	ModbusFieldConfig(  # Volumenstrom Warmwasser S18
		name="hot_water_volume_flow_s18",
		address=33041,
		unit="l/min",
		device_class=None,
		state_class="measurement",
		supported_version=1,  # SC3
		poll_time=0,
	),
	ModbusFieldConfig(  # Volumenstrom Warmwasser S18
		name="hot_water_volume_flow_s18",
		address=33041,
		unit="l/min",
		device_class=None,
		state_class="measurement",
		supported_version=2,  # SC2
		data_processing=2,
		multiplier=1,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Betriebsart
		name="hkr1_betriebsart",
		address=2818,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		options=("2", "3", "4", "5", "6", "7"),
		input_type=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Warmwasser Vorrang
		name="hkr1_warm_water_priority",
		address=2817,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		input_type=3,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Vorlaufart
		name="hkr1_vorlaufart",
		address=2819,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		enabled_by_default=False,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Fix Vorlauf Tag
		name="hkr1_fix_vorlauf_tag",
		address=2820,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		input_type=2,
		range_data=(5, 75),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Fix Vorlauf Nacht
		name="hkr1_fix_vorlauf_nacht",
		address=2821,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 75),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Heizkurve Tag Temp. 1
		name="hkr1_heizkurve_temp_tag_1",
		address=2822,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 50),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Heizkurve Tag Temp. 2
		name="hkr1_heizkurve_temp_tag_2",
		address=2823,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Heizkurve Tag Temp. 3
		name="hkr1_heizkurve_temp_tag_3",
		address=2824,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Heizkurve Absenkung
		name="hkr1_heizkurve_temp_absenkung",
		address=2825,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR1 Heizkurve Steilheit
		name="hkr1_heizkurve_steilheit",
		address=2826,
		unit=None,
		device_class=None,
		state_class="measurement",
		register=2,
		multiplier=0.01,
		edit=True,
		input_type=2,
		range_data=(0.2, 2.5),
		step_size=0.05,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Raumtemperatur_HKR1
		name="raumtemperatur_hkr1",
		address=34304,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		range_data=(0, 40),
		poll_time=0,
	),
	ModbusFieldConfig(  # A9 Mischer Heizkreis 1 zu
		name="hkr1_mischer_heizkreis_zu_a9",
		address=33288,
		state_class="measurement",
		device_class=None,
		poll_time=0,
		unit="%",
		suggested_precision=0,
		multiplier=0.001,
	),
	ModbusFieldConfig(  # A8 Mischer Heizkreis 1 auf
		name="hkr1_mischer_heizkreis_auf_a8",
		address=33287,
		state_class="measurement",
		device_class=None,
		poll_time=0,
		unit="%",
		suggested_precision=0,
		multiplier=0.001,
	),
	ModbusFieldConfig(  # HKR2 Betriebsart
		name="hkr2_betriebsart",
		address=3074,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		options=("2", "3", "4", "5", "6", "7"),
		conf_option=1,
		input_type=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Vorlaufart
		name="hkr2_vorlaufart",
		address=3075,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		conf_option=1,
		enabled_by_default=False,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Warmwasser Vorrang
		name="hkr2_warmwasser_vorrang",
		address=3073,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		input_type=3,
		conf_option=1,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Fix Vorlauf Tag
		name="hkr2_fix_vorlauf_tag",
		address=3076,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 75),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Fix Vorlauf Nacht
		name="hkr2_fix_vorlauf_nacht",
		address=3077,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 75),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Heizkurve Tag Temp. 1
		name="hkr2_heizkurve_temp_tag_1",
		address=3078,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 50),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Heizkurve Tag Temp. 2
		name="hkr2_heizkurve_temp_tag_2",
		address=3079,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Heizkurve Tag Temp. 3
		name="hkr2_heizkurve_temp_tag_3",
		address=3080,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Heizkurve Absenkung
		name="hkr2_heizkurve_temp_absenkung",
		address=3081,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR2 Heizkurve Steilheit
		name="hkr2_heizkurve_steilheit",
		address=3082,
		unit=None,
		device_class=None,
		state_class="measurement",
		register=2,
		multiplier=0.01,
		edit=True,
		input_type=2,
		range_data=(0.2, 2.5),
		conf_option=1,
		step_size=0.05,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Raumtemperatur_HKR2
		name="raumtemperatur_hkr2",
		address=34305,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		range_data=(0, 40),
		conf_option=1,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Betriebsart
		name="hkr3_betriebsart",
		address=3330,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		options=("2", "3", "4", "5", "6", "7"),
		conf_option=2,
		input_type=1,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Vorlaufart
		name="hkr3_vorlaufart",
		address=3331,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		conf_option=2,
		enabled_by_default=False,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Warmwasser Vorrang
		name="hkr3_warmwasser_vorrang",
		address=3329,
		unit=None,
		device_class=None,
		state_class=None,
		register=2,
		multiplier=1,
		input_type=3,
		conf_option=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Fix Vorlauf Tag
		name="hkr3_fix_vorlauf_tag",
		address=3332,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		range_data=(5, 75),
		conf_option=2,
		input_type=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Fix Vorlauf Nacht
		name="hkr3_fix_vorlauf_nacht",
		address=3333,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 75),
		conf_option=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Heizkurve Tag Temp. 1
		name="hkr3_heizkurve_temp_tag_1",
		address=3334,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 50),
		conf_option=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Heizkurve Tag Temp. 2
		name="hkr3_heizkurve_temp_tag_2",
		address=3335,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Heizkurve Tag Temp. 3
		name="hkr3_heizkurve_temp_tag_3",
		address=3336,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=2,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Heizkurve Absenkung
		name="hkr3_heizkurve_temp_absenkung",
		address=3336,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(5, 30),
		conf_option=2,
		poll_time=0,
	),
	ModbusFieldConfig(  # HKR3 Heizkurve Steilheit
		name="hkr3_heizkurve_steilheit",
		address=3338,
		unit=None,
		device_class=None,
		state_class="measurement",
		register=2,
		multiplier=0.01,
		edit=True,
		input_type=2,
		range_data=(0.2, 2.5),
		conf_option=2,
		step_size=0.05,
		poll_rate=True,
		poll_time=0,
	),
	ModbusFieldConfig(  # Raumtemperatur_HKR3
		name="raumtemperatur_hkr3",
		address=34306,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		range_data=(0, 40),
		conf_option=2,
		poll_time=0,
	),
	ModbusFieldConfig(  # WW Solltemperatur
		name="ww_solltemperatur",
		address=2305,
		unit="°C",
		device_class="temperature",
		state_class="measurement",
		register=2,
		multiplier=1,
		edit=True,
		input_type=2,
		range_data=(10, 65),
		poll_time=0,
	),
	ModbusFieldConfig(  # VersionSC
		name="version_sc",
		address=32770,
		unit=None,
		device_class=None,
		state_class=None,
		multiplier=1,
		entity_category="diagnostic",
		data_processing=1,
		poll_rate=True,
		poll_time=0,
		suggested_precision=None,
	),
	ModbusFieldConfig(  # VersionNBG
		name="version_nbg",
		address=32771,
		unit=None,
		device_class=None,
		state_class=None,
		multiplier=1,
		entity_category="diagnostic",
		data_processing=1,
		poll_rate=True,
		poll_time=0,
		suggested_precision=None,
	),
	ModbusFieldConfig(
		name="digin_error",
		address=33045,
		unit=None,
		device_class=None,
		state_class=None,
		multiplier=1,
		entity_category="diagnostic",
		poll_time=0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # ZirkulationBetriebsart
		name="zirkulation_betriebsart",
		address=2049,
		unit=None,
		device_class=None,
		state_class=None,
		multiplier=1,
		poll_time=0,
	),
	ModbusFieldConfig(  # Wärmepumenleistung
		name="waermepumpe_leistung",
		address=33544,
		unit="kW",
		device_class="power",
		state_class="measurement",
		register=2,
		edit=False,
		conf_option=4,
		poll_time=0,
	),
	ModbusFieldConfig(  # elektrische Wärmepumenleistung
		name="elek_waermepumpe_leistung",
		address=33545,
		unit="kW",
		device_class="power",
		state_class="measurement",
		register=2,
		edit=False,
		conf_option=4,
		poll_time=0,
	),
	ModbusFieldConfig(  # Umschaltventil Wärmepumpe A14
		name="umschaltventil_waermepumpe_a14",
		address=33293,
		unit="%",
		state_class="measurement",
		device_class=None,
		conf_option=4,
		poll_time=0,
		byte_swap=1,
		multiplier=1.0,
		suggested_precision=0,
	),
	ModbusFieldConfig(  # Wärmemengenzähler Leistung
		name="wmz_leistung",
		address=33550,
		unit="kW",
		state_class="measurement",
		device_class="power",
		poll_time=0,
	),  # Added with #121
]
