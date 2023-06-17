import { updateField } from 'vuex-map-fields';
import jsonLogic from 'json-logic-js';
export { updateField }

import { merge, mergeWith } from 'lodash';
import { _ } from 'core-js';

export function mutate_auth (state, auth) {
    state.auth = auth
}

export function switch_server (state, serverdata) {
    console.log(serverdata)
    try {
        state.userdata.servers[serverdata._id] = {'selected_room': serverdata.default_room};
        state.userdata.state.selected_room = serverdata.default_room
        state.userdata.state.selected_server = serverdata._id
        state.serverdata = serverdata;
    } catch (error) {
        console.log(error)
    }
}


export function mutate_set(state, update) {
    console.log(update)
    _.set(state, update.string, update.value)
}



export function mutate_deep(state, deep_update) {
    merge(state, deep_update)
    console.log('DEEP UPDATE', deep_update);
    
}


export function mutate_deep_arrayset(state, deep_update) {
    function customizer(objValue, srcValue) {
        if (_.isArray(objValue)) {
          return srcValue;
        }
      }
    mergeWith(state, deep_update, customizer)
    console.log('DEEP UPDATE', deep_update);
    
}

export function mutate_shallow(state, shallow_update) {
    
    Object.keys(shallow_update).forEach(
      (prop) => (state[prop] = shallow_update[prop])
    );
    console.log('SHALLOW UPDATE', shallow_update);
}


export function socket_updates(state, update) {
    update = JSON.parse(update)
    
    if(update.operation == 'push') {
        mergeWith(state, update.data, customizer);
    }
    else merge(state, update.data)
}



export function mutate_logic_create(state, update) {
    console.log(`logic.if${update.path}`, update.value)
    console.log(_.set(state, `logic.${update.path}`, update.value))
}


function get_progress(state, workspace_id, board_id, task_id, board) {
    let status_mapping = {
        'Done': 100,
        'Doing': 50,
        'Stuck': 25,
        'Pending': 0
    }
    function iterate_progress(update_task_id, task) {
        let result = task.completion_dependency.ends_with_required.reduce((prev, curr)=>{
            prev += board.task[curr]?.progress || status_mapping?.[board.task[curr]?.status] || 0;
            return prev
        }, 0)
        mutate_task(state, {
            workspace_id: workspace_id,
            board_id: board_id,
            task_id: update_task_id,
            attr: 'progress',
            value: result/task.completion_dependency.ends_with_required.length,
            operation: 'set'
            }
        )
        }
        Object.entries(board.task).forEach(task => {
            if(task[1]?.completion_dependency.ends_with_required.includes(task_id)) {
                iterate_progress(task[0], task[1])
        }
    })
}



export function mutate_task(state, update) {
    if(['number', 'text','color', 'date', 'daterange', 'resource', 'involved', 'checkbox'].includes(update?.type)) {
        if(state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.type] == null) {
            state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.type] = {
                [update.attr]: null
            }
        }
        var mutatee = state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.type]
    }
    else {
        var mutatee = state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id]
    }
 
	switch(update.operation) {
        case 'merge':
            merge(mutatee, {[update.attr]: update.value})
        break;
        case 'set':
            // state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.attr][update.type] = update.value
            mutatee[update.attr] = update.value
        break;
		case 'push':
			state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.attr].push(update.value)
		break;
		case 'splice':
			state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id][update.attr].splice(update.index, 1)
		break;
        case 'increment':
            mutatee[update.attr] += 2
	}
    let mutations = {
        'mutate_task': mutate_task
    }
    // if(jsonLogic.apply({'==': [{'var': 'value' }, 'Done']}, update)) {
        
    //     let operation = {
    //         mutation: 'mutate_task',
    //         arguments: {
    //             workspace_id: update.workspace_id,
    //             board_id: update.board_id,
    //             task_id: update.task_id,
    //             attr: 'progress',
    //             value: 100,
    //             operation: 'set'
    //         }
    //     }
    //     mutations[operation.mutation](state, operation.arguments)
    // }
    // if(jsonLogic.apply({'==': [{'var': 'value' }, 100]}, update)) {
        
    //     let operation = {
    //         mutation: 'mutate_task',
    //         arguments: {
    //             workspace_id: update.workspace_id,
    //             board_id: update.board_id,
    //             task_id: update.task_id,
    //             attr: 'status',
    //             value: 'Done',
    //             operation: 'set'
    //         }
    //     }
    //     mutations[operation.mutation](state, operation.arguments)
    // }

    /*
    UPDATE MIRRORS
    */
    let incoming_refs = state.workspacedata[update.workspace_id].board[update.board_id].task[update.task_id].meta?.incoming_ref?.[update.attr]
    incoming_refs ? incoming_refs.forEach(ele=> {
        let update_mirror = {
            workspace_id: ele?.w || update.workspace_id,
            board_id: ele.b,
            task_id: ele.t,
            attr: ele.linked_field,
            value: update.value,
            operation: update.operation
        }
        console.log(update_mirror)
        mutate_task(state, update_mirror)
    }) : null

    // if(update.attr == 'progress') get_progress(
    //     state,
    //     update.workspace_id,
    //     update.board_id,
    //     update.task_id,
    //     state.workspacedata[update.workspace_id].board[update.board_id],
    //     );
}




export function mutate_field(state, update) {
	switch(update.operation) {
		case 'push':
			state.workspacedata[update.workspace_id].field[update.field][update.attr].push(update.value)
		break;
		case 'splice':
			state.workspacedata[update.workspace_id].field[update.field][update.attr].splice(update.index, 1)
		break;
	}
    
}





export function mutate_cytograph_elements(state, jsonele) {
    state.cytograph.json({ elements: jsonele });
    this.commit("refresh_cytograph");
  }



























export function someMutation (state) {
    state.data = 1
}

export function update_serialized_permissions(state, serialized_permissions) {
    state.form_role.permissions = serialized_permissions
}

export function set_is_logged_in(state) {
    state.logged_in = true;
}

export function set_admin_selected_menu(state, menu) {
    state.admin_selected_menu = menu;
}

export function mutate_permissions(state) {
    state.selected_serverdata.permissions = 4294967295;
}




export function push_serverdata(state, push_update) {
    state = merge(state, push_update, { arraypush: true });
}

export function set_selected_room(state, room) {
    state.selected_room = room;
}

export function set_selected_emoticon(state, emoticon) {
    [state.selected_group, state.selected_emoticon] = emoticon;
}

export function push_incoming_chat(state, message) {
    state.selected_roomdata.posts.push({
      content: message,
      posted_by: "id",
      date: "date",
      id: "id",
      reply_to: "null",
    });
}