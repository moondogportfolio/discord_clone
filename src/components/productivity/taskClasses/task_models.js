// class NumberMeta(BaseModel):
// 	fieldname: str
// 	default_field_name = 'number'
// 	default_label = 'Number'
// 	type = 'number'
// 	default: Optional[int]
// 	unit: str
// 	max: int
// 	min: int
// 	position: int = 0
// 	details: Optional[str]

// class TextMeta(BaseModel):
// 	fieldname: str
// 	default_field_name = 'text'
// 	default_label = 'Text'
// 	type = 'text'
// 	default: str
// 	max_len: int
// 	min_len: int
// 	position: int = 0
// 	details: Optional[str]

export let fields = {
    number: 'Number',
    text: 'Text',
    color: 'Color',
    checkbox: 'Checkbox',
    status: 'Status',
}

export function number_meta (index, position) {
    return {
        fieldname: `number-${index}`,
        label: index == 0? 'Number': `Number ${index}`,
        type: 'number',
        position: position
    }
}

export function text_meta (index, position) {
    return {
        fieldname: `text-${index}`,
        label: index == 0? 'Text': `Text ${index}`,
        type: 'text',
        position: position
    }
}

export function color_meta (index, position) {
    return {
        fieldname: `color-${index}`,
        label: index == 0? 'Color': `Color ${index}`,
        type: 'color',
        position: position
    }
}

export function daterange_meta (index, position) {
    return {
        fieldname: `daterange-${index}`,
        label: index == 0? 'Date Range': `Date Range ${index}`,
        type: 'daterange',
        position: position
    }
}

export function checkbox_meta (index, position, value_type="single") {
    return {
        fieldname: `checkbox-${index}`,
        label: index == 0? 'Checkbox': `Checkbox ${index}`,
        type: 'checkbox',
        position: position,
        value_type: value_type 
        // value_type options single, dict, list
    }
}

export var constructor_dict = {
    'number': number_meta,
    'text': text_meta,
    'color': color_meta,
    'daterange': daterange_meta,
    'checkbox': checkbox_meta
  }