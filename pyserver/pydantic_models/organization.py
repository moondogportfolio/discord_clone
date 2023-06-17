from devtools import debug
from pydantic_models.universal import ObjectIdStr
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime, timedelta


class DateRange(BaseModel):
	'''
	optional datetime, for +inf range
	'''
	start: datetime
	end: Optional[datetime]


class EntityAllocation(BaseModel):
	container: ObjectIdStr
	task: ObjectIdStr
	allocation: ObjectIdStr


class TaskScheduleIn(BaseModel):
	daterange: DateRange
	hardcap: Optional[datetime]
	hours: Optional[int]


class TaskSchedule(TaskScheduleIn):
	override: Optional[List[ObjectIdStr]]



class EntityTask(BaseModel):
	daterange: Optional[DateRange]
	override: Optional[List[ObjectIdStr]]
	permission: Optional[int]
	#display purposes
	tasktitle: str
	schedule: Optional[Dict[ObjectIdStr, TaskSchedule]]


class EntityPartial(BaseModel):
	name: str
	role: Optional[str]

class EntityGroup(BaseModel):
	name: str
	member: Dict[ObjectIdStr, EntityPartial]
	relationship: Optional[Dict[ObjectIdStr, str]]
	allocation: Optional[List[EntityAllocation]]
	task: Optional[Dict[ObjectIdStr, EntityTask]]
