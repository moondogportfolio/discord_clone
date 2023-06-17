	export default function (task_name, api, auth, board_id, workspace_id) {
	api({
		method: 'post',
		url: `/workspace/${workspace_id}/board/${board_id}/task`,
		data: {
			type: 1,
			board: board_id,
			tasktitle: task_name
		},
		headers : {
		'Content-Type': 'application/json',
		Authorization: `Bearer ${auth}`
		}
		}).then((response)=>{
			console.log(response);
		}).catch((error) => {
			null
		})
	}
