from devtools import debug
from pydantic_models.universal import Permission, PermissionBitflag, ObjectIdStr, ObjectId_Model, ObjectIdFactory
from datetime import date, datetime
from typing import List, Dict, Union, Optional
from pydantic import BaseModel, Field, root_validator
from enum import Enum, auto, IntEnum





# class Condition(BaseModel):
# 	pass

# class Dependencies(BaseModel):
# 	task_id: ObjectIdStr
# 	from_status: str
# 	to_status: str
# 	conditions: List[Condition]


# class PeriodicalDateHistory(BaseModel):
# 	daterange: DateRange
# 	status: str

# class PeriodicalDate(BaseModel):
# 	period: int #seconds
# 	daterange: DateRange
# 	history: List[PeriodicalDateHistory]

# class TrackedTime(BaseModel):
# 	daterange: DateRange
# 	type: str #manual, automatic



# class Involved(BaseModel):
# 	_id: ObjectIdStr
# 	role: str #todo




# class Categories(BaseModel):
# 	value: str
# 	fieldname: str


# class TaskGroup(BaseModel):
# 	groupname: str
# 	index: str

class InvolvedType(IntEnum):
	INDIVIDUAL = auto()
	ROLE = auto()
	# GUEST = auto()
	# COMPANY = auto()

class Involved(BaseModel):
	entity: ObjectIdStr
	type: InvolvedType
	position: str


class TaskTypeEnum(IntEnum):
	TASK = auto()
	GOAL = auto()




class CompletionDependency(BaseModel):
	ends_with_required: Optional[List[ObjectIdStr]]
	ends_with: Optional[List[ObjectIdStr]]

class TaskCreate(BaseModel):
	type: TaskTypeEnum
	board: ObjectIdStr
	tasktitle: str
	details: Optional[str]
	comments: Optional[str]
	status: Optional[str]
	group: List[str] = []
	granularity: Optional[int]
	involved: List[Involved] = []
	tag: List[str] = []
	position: Optional[int] = 0
	completion_dependency: Optional[Dict[str, CompletionDependency]]
	
	class Config: 
		use_enum_values = True

class TaskModify(TaskCreate):
	type: Optional[TaskTypeEnum]
	tasktitle: Optional[str]

	class Config: 
		use_enum_values = True

class Task(TaskCreate):
	creator: ObjectIdStr
	history: List = []

	



class BoardIn(BaseModel):
	name: str = Field(..., example = 'Example Board')
	index: int = 0

class Board(BaseModel):
	_id: ObjectIdStr
	name: str
	task: Dict[ObjectIdStr, Task] = {}
	index: str



class Category(BaseModel):
	name: str
	color: str


class StatusMeta(BaseModel):
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

class GroupMeta(BaseModel):
	options: Optional[List[str]] = []
	label = 'Group'
	fieldname = 'group'
	position: int = 0
	details: Optional[str]
	default: List = []
	type = 'group'


class GranularityMeta(BaseModel):
	label = 'Granularity'
	fieldname = 'granularity'
	position: int = 0
	details: Optional[str]
	default: Optional[int] = None
	min = 0
	max = 5
	type="granularity"

class InvolvedMeta(BaseModel):
	label = 'Involved'
	fieldname = 'involved'
	roles: List[str] = ['Assigned', 'Administrator']
	details: Optional[str]
	position: int = 0
	type="involved"


class TagMeta(BaseModel):
	options: Optional[List[str]] = []
	label = 'Tags'
	fieldname = 'tag'
	position: int = 0
	details: Optional[str]
	default: Optional[str] = None
	type = "tag"


class ScoreCardMeta(BaseModel):
	default = ['User experience', 'Performance gains']

class NumberMeta(BaseModel):
	default_field_name = 'number'
	default_label = 'Number'

class TextMeta(BaseModel):
	default_field_name = 'text'
	default_label = 'Text'


class ColorMeta(BaseModel):
	default_field_name = 'color'
	default_label = 'Color'

class CheckboxMeta(BaseModel):
	default_field_name = 'checkbox'
	default_label = 'Checkbox'

class CompletionDependencyMeta(BaseModel):
	default_field_name = 'completion_dependency'
	default_label = 'Completion Dependency'

class DateRange(BaseModel):
	start: datetime
	end: datetime



class TimetrackerMeta(BaseModel):
	default_field_name = 'timetracker'
	default_label = 'Timetracker'

class LocationMeta(BaseModel):
	location: str


class PeriodicalDateMeta:
	default_field_name = 'periodicalrange'
	default_label = 'Periodical Range'

class DateMeta(BaseModel):
	default_label = 'Date'
	type = 'date'

class DateRangeMeta(BaseModel):
	default_field_name = 'daterange'
	default_label = 'Date Range'

