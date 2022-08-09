import copy
import random
import socket
from graphviz import Digraph


# This method generate a data structure which represent one state and its three transitions
def generate_states():
    # create a Digraph
    dot = Digraph(name="state machine structure", format="png")
    states = ['A']  # A always be the first in the states
    dot.node(name='A', label='A', color='Black')
    # random the states
    i = 0
    while i < 24:
        letter = chr(random.randint(65, 89))
        if letter in states:
            continue;
        else:
            states.append(letter)
            i = i + 1
    states.append('Z')
    print('The initial 26 states are as follow: ')
    print(states)

    states_dict = {}
    actions = ['1', '2', '3']
    edge_list = []
    for i in range(0, states.__len__() - 1):
        edge_list.clear()
        if i < states.__len__() - 3:
            f_edge = states[i + 1]
            s_edge = states[i + 2]
            t_edge = states[i + 3]
        elif i == states.__len__() - 3:
            f_edge = states[i + 1]
            s_edge = states[0]
            t_edge = states[1]
        elif i == states.__len__() - 2:
            f_edge = states[0]
            s_edge = states[1]
            t_edge = states[2]
        random.shuffle(actions)  # random the actions
        f_edge_action = actions[0] + '->' + f_edge
        s_edge_action = actions[1] + '->' + s_edge
        t_edge_action = actions[2] + '->' + t_edge
        edge_list.append(f_edge_action)
        edge_list.append(s_edge_action)
        edge_list.append(t_edge_action)
        states_dict[states[i]] = edge_list
        states_dict.update({states[i]: copy.deepcopy(edge_list)})
        # begin draw the point
        dot.node(name=f_edge, label=f_edge, color='Black')
        dot.node(name=s_edge, label=s_edge, color='Black')
        dot.node(name=t_edge, label=t_edge, color='Black')
        # draw line between point，label：action
        dot.edge(states[i], f_edge, label=actions[0], color='red')
        dot.edge(states[i], s_edge, label=actions[1], color='red')
        dot.edge(states[i], t_edge, label=actions[2], color='red')
    dot.view(filename="state machine structure", directory="")
    print(states_dict)
    # 'A': ['3->B', '1->C', '2->D'] means that if server receive request 3 from client, state A will transform to
    # state B; if server receive request 1 from client, state A will transform to state C; if server receive request 2
    # from client, state A will transform to state D;
    return states_dict


if __name__ == "__main__":
    state_dict = generate_states()
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '127.0.0.1'
    host = '20.211.33.233'
    port = 65432
    socketServer.bind((host, port))
    socketServer.listen(5)
    clientSocket, addr = socketServer.accept()
    print('Connection established')
    print('Server:A' + '\n')
    current_server = 'A'
    while True:
        # receive request from client
        recvMsg = clientSocket.recv(1024)
        # decode the received data
        strData = recvMsg.decode("utf-8")
        print("Client:" + strData)
        # according to actions to do transitions
        edges_list = copy.deepcopy(state_dict[current_server])
        for i in range(0, edges_list.__len__()):
            if edges_list[i].__contains__(strData):
                array = edges_list[i].split('->')
                current_server = array[1]
            else:
                continue
        msg = current_server
        print('Server:' + msg + '\n')
        if msg == 'Z':
            print('Server:A' + '\n')
            current_server = 'A'
        # code the sending data
        else:
            msg = msg + '\n'
        clientSocket.send(msg.encode("utf-8"))
