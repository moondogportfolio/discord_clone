from pydantic_models.resource import Transaction, ResourceContainer
from pydantic_models.organization import EntityGroup
from devtools import debug
from pydantic_models.universal import ObjectIdStr
from datetime import date, datetime, time, timedelta
from typing import List, Dict, Union, Optional, Any
from pydantic import BaseModel, Field, root_validator, validator
from enum import Enum, auto, IntEnum






class TaskTypeEnum(Enum):
	TASK = auto()
	MILESTONE = auto()



class DateRange(BaseModel):
	'''
	optional datetime, for +inf range
	'''
	start: datetime
	end: Optional[datetime]

class TaskCompletionDependency(BaseModel):
	ends_with_required: Optional[List[ObjectIdStr]]
	ends_with: Optional[List[ObjectIdStr]]

class Activity(BaseModel):
	content: str
	files: List[ObjectIdStr]





class TaskIn(BaseModel):
	# activity: Activity
	# 
	type: TaskTypeEnum
	board: ObjectIdStr
	tasktitle: str
	completion_dependency: Optional[TaskCompletionDependency]
	details: Optional[str]
	comments: Optional[str]
	status: Optional[str]
	progress: Optional[int]
	group: Optional[List[str]]
	granularity: Optional[int]
	tag: Optional[List[str]]
	position: Optional[int] = 0
	resource: Optional[Dict[str, int]]
	# involved: 
	date: Optional[Dict[str, datetime]]
	daterange: Optional[Dict[str, DateRange]]


	class Config: 
		use_enum_values = True

class TaskModify(TaskIn):
	type: Optional[TaskTypeEnum]
	board: Optional[ObjectIdStr]
	tasktitle: Optional[str]

	class Config: 
		use_enum_values = True

class BoardDeltaOperationEnum(Enum):
	CREATED_TASK= auto()
	MODIFIED_TASK_VALUE= auto()
	MODIFIED_TASK_VALUE_SET= auto()
	MODIFIED_TASK_VALUE_PUSH= auto()
	MODIFIED_TASK_VALUE_PULL= auto()
	MODIFIED_TASK_VALUE_UNSET= auto()
	DELETED_TASK= auto()
	CREATED_FIELD= auto()
	MODIFIED_FIELD= auto()
	DELETED_FIELD= auto()
	CREATED_BOARD= auto()
	DELETED_BOARD= auto()
	OPERATION_REQUEST= auto()
	OPERATION_REVIEW= auto()
	OPERATION_GRANT= auto()

class BoardEntityEnum(Enum):
	TASK= auto()
	FIELD= auto()
	BOARD= auto()



class ReferenceOut(BaseModel):
	w: Optional[ObjectIdStr]
	b: Optional[ObjectIdStr]
	t: Optional[ObjectIdStr]


class ReferenceIn(BaseModel):
	w: Optional[ObjectIdStr]
	b: Optional[ObjectIdStr]
	t: Optional[ObjectIdStr]
	linked_field: Optional[str]

class ReferenceTango(BaseModel):
	self_field: str
	workspace_ref: Optional[ObjectIdStr]
	board_ref: Optional[ObjectIdStr]
	task_ref: Optional[ObjectIdStr]
	linked_field: Optional[str]

class BoardDeltaPermission(BaseModel):
	date: datetime
	initiator: ObjectIdStr

class BoardDelta(BaseModel):
	date: datetime = datetime.now()
	operation: BoardDeltaOperationEnum
	old_val: Optional[Union[str, int]]
	new_val: Optional[Union[str, int]]
	obj: BoardEntityEnum
	obj_id: ObjectIdStr
	attribute: str
	request: Optional[BoardDeltaPermission]
	approval: Optional[BoardDeltaPermission]

	class Config: 
		use_enum_values = True

class TaskCycle(BaseModel):
	daterange: DateRange
	timedelta: Optional[int] # seconds; no value means autorefreshes instantly
	override: Optional[ObjectIdStr]

class CycleModeEnum(Enum):
	ARCHIVE_AND_CREATE_NEW = auto()
	ARCHIVE_AND_RESET = auto()


class TaskCycleHistoryEntry(BaseModel):
	completed: datetime = datetime.now()
	values: Optional[TaskIn]
	cycle_index: int
	operation_after: CycleModeEnum

	class Config: 
		use_enum_values = True


class TaskCycleHistory(BaseModel):
	entries: List[TaskCycleHistoryEntry]
	streak: Optional[int]

class TaskMeta(BaseModel):
	creator: ObjectIdStr
	created: Optional[datetime] = datetime.now()
	history: Optional[Dict[ObjectIdStr, TaskCycleHistoryEntry]] #id = cycle id
	cycles: Optional[Dict[ObjectIdStr, TaskCycle]] #id = cycle id
	outgoing_ref: Optional[Dict[str, List[ReferenceOut]]]
	incoming_ref: Optional[Dict[str, List[ReferenceIn]]]
	twoway_ref: Optional[List[ReferenceTango]]


class NewCycleModeEnum(Enum):
	CYCLE_END = auto()
	STATUS_COMPLETE = auto()


class TaskSettings(BaseModel):
	cycle_mode: CycleModeEnum
	new_cycle_mode: NewCycleModeEnum

class Task(TaskIn):
	meta: TaskMeta
	settings: Optional[TaskSettings]
	





class Category(BaseModel):
	name: str
	color: str


class StatusField(BaseModel):
	options: List[Category] = [
		Category.construct(**item) for item in
		[{'name':'Done', 'color':'green'}, {'name':'Doing', 'color':'yellow'}, {'name':'Stuck', 'color':'red'}, {'name':'Pending', 'color':'grey'}
		]]
	done: List[str] = ['Done']
	label = 'Status'
	fieldname = 'status'
	position: int = 0
	details: Optional[str]
	default: str = 'Pending'
	type = 'status'

class GroupField(BaseModel):
	options: Optional[List[str]] = []
	label = 'Group'
	fieldname = 'group'
	position: int = 0
	details: Optional[str]
	default: List = []
	type = 'group'

class ProgressField(BaseModel):
	label = 'Progress'
	fieldname = 'progress'
	position: int = 0
	details: Optional[str]
	type = 'progress'


class GranularityField(BaseModel):
	label = 'Granularity'
	fieldname = 'granularity'
	position: int = 0
	details: Optional[str]
	default: Optional[int] = None
	min = 0
	max = 5
	type="granularity"


class TagField(BaseModel):
	options: Optional[List[str]] = []
	label = 'Tags'
	fieldname = 'tag'
	position: int = 0
	details: Optional[str]
	default: Optional[str] = None
	type = "tag"


class ScoreCardMeta(BaseModel):
	options: Optional[List[str]] = []
	label = 'Scorecard'
	fieldname = 'scorecard'
	position: int = 0
	details: Optional[str]
	default = ['User experience', 'Performance gains']
	type="scorecard"

class NumberMeta(BaseModel):
	fieldname: str
	type = 'number'
	default: Optional[int]
	unit: str
	max: int
	min: int
	position: int = 0
	details: Optional[str]

class TextMeta(BaseModel):
	fieldname: str
	type = 'text'
	default: str
	max_len: int
	min_len: int
	position: int = 0
	details: Optional[str]


class InvolvedField(BaseModel):
	fieldname: str = 'involved'
	label: str = 'Responsible'
	add_to_workload: bool = True
	details: Optional[str]
	position: int = 0
	type="involved"
	default: Optional[List] = []


class ColorMeta(BaseModel):
	fieldname: str
	options: List[str]
	type = 'color'
	position: int = 0
	details: Optional[str]

class CheckboxMeta(BaseModel):
	fieldname: str
	null_option: bool = False
	type = 'checkbox'
	position: int = 0
	details: Optional[str]

class CompletionDependencyField(BaseModel):
	fieldname: str
	null_option: bool = False
	type = 'completion_dependency'
	position: int = 0
	details: Optional[str]
	label: str




class TimetrackerMeta(BaseModel):
	fieldname: str
	null_option: bool = False
	type = 'timetracker'
	position: int
	daterange: DateRange
	details: Optional[str]

class LocationMeta(BaseModel):
	location: str


class DateField(BaseModel):
	fieldname: str
	type = 'date'
	position: int = 0
	daterange: Optional[DateRange]
	label: str

class DateRangeField(BaseModel):
	fieldname: str
	type = 'daterange'
	position: int = 0
	daterange: Optional[DateRange]
	label: str


class ResourceField(BaseModel):
	fieldname: str = 'days'
	label: str = 'Days'
	type = 'resource'
	position: int = 0
	resource: ObjectIdStr


class WorkspaceFields(BaseModel):
	#one to one
	status: Optional[StatusField]
	progress: Optional[ProgressField]
	group: Optional[GroupField]
	completion_dependency: Optional[CompletionDependencyField]
	granularity: Optional[GranularityField]
	involved: Optional[List[InvolvedField]]
	tag: Optional[TagField] 
	daterange: Optional[List[DateRangeField]]
	date: Optional[List[DateField]]
	resource: Optional[List[ResourceField]]

	@root_validator(pre=True)
	def _status_prevalidator(cls, values):
		default_dict = {
			'status': StatusField.construct(),
			'group': GroupField.construct(),
			'granularity': GranularityField.construct(),
			'involved': InvolvedField.construct(),
			'tag': TagField.construct(),
			'daterange': DateRangeField.construct(),
			'date': DateField.construct(),
			'completion_dependency': CompletionDependencyField.construct(),
			'progress': ProgressField.construct(),
			'resource': ResourceField.construct()
		}
		grouped_field = [
			'daterange', 'date', 'resource', 'involved'
		]
		for v in values.keys():
			if v in grouped_field and values[v] == 'default':
				values[v] = [default_dict[v]]
			elif values[v] == 'default':
				values[v] = default_dict[v]
		return values
		



	# dependencies: Optional[DependencyMeta]
	#one to many
	# text: List[TextMeta]
	# number: List[NumberMeta]
	# color: List[ColorMeta]
	# bools: List[BoolsMeta]
	# location: List[LocationMeta]
	# #dates, one to many
	# daterange: List[DateRangeMeta]
	# timetracker: List[TimetrackerMeta]
	# periodicalrange: List[PeriodicalDateMeta]


class WorkspaceIn(BaseModel):
	name: str




class TimeRange(BaseModel):
	start: time
	end: time

	@root_validator()
	def datetime_to_string(cls, values):
		try:
			values['start'] = values['start'].isoformat(timespec="minutes")
			values['end'] = values['end'].isoformat(timespec="minutes")
		except:
			raise ValueError
		return values


class MemberAvailability(BaseModel):
	start: datetime
	end: Optional[datetime]
	mon: Optional[TimeRange]
	tue: Optional[TimeRange]
	wed: Optional[TimeRange]
	thu: Optional[TimeRange]
	fri: Optional[TimeRange]
	sat: Optional[TimeRange]
	sun: Optional[TimeRange]
	position: Optional[int]

	



class BoardIn(BaseModel):
	name: str = Field(..., example = 'Example Board')
	index: int = 0

class Board(BaseModel):
	_id: ObjectIdStr
	name: str
	task: Dict[ObjectIdStr, Task] = {}
	index: str
	field: WorkspaceFields = {}
	delta: List[BoardDelta]

class MemberIn(BaseModel):
	availability_rules: List[MemberAvailability]

class Member(MemberIn):
	join_date: Optional[datetime]

class Workspace(WorkspaceIn):
	_id: ObjectIdStr
	board: Dict[ObjectIdStr, Board] = {}
	resource_container: Optional[Dict[ObjectIdStr, ResourceContainer]]
	transaction: Optional[Dict[ObjectIdStr,Transaction]]
	entity_group: Optional[Dict[ObjectIdStr, EntityGroup]]



class TimeSheetEntry(BaseModel):
	project: ObjectIdStr
	task: ObjectIdStr
	schedule: datetime
	duration: int


