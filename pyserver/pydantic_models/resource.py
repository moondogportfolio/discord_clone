from pydantic import BaseModel
from pydantic.utils import Obj
from pydantic_models.universal import ObjectIdStr
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum, auto
from datetime import datetime, timedelta


class BaseMetadata(BaseModel):
	created: datetime
	creator: ObjectIdStr

class InvolvedResource(BaseModel):
    amount: int
    internal_id: Optional[ObjectIdStr]
    description: Optional[str]
    method: Optional[str]
    transfer_date: Optional[datetime] #no transfer_date assumes transfer is same as tx date
    entity: Optional[ObjectIdStr]
    details: Optional[Dict]

# class TransactionTypeEnum(Enum):
#     SALE:
#     PURCHASE:
#     REFUND:
#     CREDIT:
#     DEBIT:
#     VOID: 

#https://account.authorize.net/help/Search/Transaction_Detail/Transaction_Detail_Page.htm
#https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/transaction_details.htm



class DateRange(BaseModel):
	'''
	optional datetime, for +inf range
	'''
	start: datetime
	end: Optional[datetime]

class Transaction(BaseModel):
    # type: TransactionTypeEnum
    status: Optional[str]
    details: Optional[str]
    initiation_date: Optional[datetime]
    settlement_date: Optional[datetime] #when all resources have been transferred
    resource_out: Optional[List[InvolvedResource]]
    resource_in: Optional[List[InvolvedResource]]
    initiator: Optional[List[ObjectIdStr]]
    approval: Optional[List[ObjectIdStr]]

    

class HardCapStrategyEnum(Enum):
	STOP_TASK = auto()
	INCUR_TO_SOURCE = auto()
	INCUR_TO_BASE_SOURCE = auto()



class AllocationSchedule(BaseModel):
	daterange: DateRange
	budget: int
	hardcap: Optional[int]
	exceed_hardcap_strategies: Optional[HardCapStrategyEnum]
	override: Optional[List[ObjectIdStr]]

	class Config: 
		use_enum_values = True


class Allocation(BaseModel):
	resource: ObjectIdStr
	entity: ObjectIdStr
	amount: int
	scheduled: int
	hardcap: Optional[int]
	exceed_hardcap_strategies: Optional[HardCapStrategyEnum]
	schedule: Optional[Dict[ObjectIdStr, AllocationSchedule]] #schedule id
    
	class Config: 
		use_enum_values = True


class FloatingAllocation(BaseModel):
	amount: int
	scheduled: int
	hardcap: Optional[int]
	exceed_hardcap_strategies: Optional[HardCapStrategyEnum]
	schedule: Optional[List[AllocationSchedule]]
    
	class Config: 
		use_enum_values = True


class ResourceRequest(BaseModel):
	amount: int
	resource: ObjectIdStr	

class ResourceDetails(BaseModel):
	max: Optional[int]
	amount: int = 0
	hardcap: Optional[int]
	exceed_hardcap_strategies: Optional[HardCapStrategyEnum]
	name: str

	class Config: 
		use_enum_values = True

class ResourceTask(BaseModel):
	name: str
	allocation: Dict[ObjectIdStr, Allocation]
	metadata: Optional[BaseMetadata]

class ResourceContainer(BaseModel):
	task: Optional[Dict[ObjectIdStr, ResourceTask]] #taskid #alloc id
	resource: Optional[Dict[ObjectIdStr, ResourceDetails]]
	entity: Optional[Dict[ObjectIdStr, FloatingAllocation]]
	name: str
	#metadata
	metadata: Optional[BaseMetadata]

class ResourceAllocation(BaseModel):
	container: ObjectIdStr
	task: ObjectIdStr
	allocation: ObjectIdStr
	metadata: Optional[BaseMetadata]


class Resource(BaseModel):
	name: str
	unit: Optional[str]
	details: Optional[Dict]
	allocation: Optional[List[ResourceAllocation]]
	metadata: Optional[BaseMetadata]