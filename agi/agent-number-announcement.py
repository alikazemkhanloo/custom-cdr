#!/usr/bin/python3

import sys
from wazo_agid.fastagi import FastAGI
from wazo_agid import agid

def main():
    fagi = FastAGI(sys.stdin.buffer, sys.stdout.buffer, {})
    
    fagi.verbose('**********  Start announcing agent number **********')
    
    try:
        agent_number = fagi.get_variable('MEMBERNAME')
        fagi.verbose(f'Agent number: {agent_number[6:]}')  # Verbose statement
        fagi.stream_file('survey/agent-number-karshenas')
        fagi.say_number(agent_number[6:])
        fagi.verbose('********** End announcing agent number **********')
    except Exception as e:
        fagi.verbose(f'Error: {e}')  # Verbose statement
        fagi.verbose(f'!!!!!!!!!! Error: {e} !!!!!!!!!!')
        fagi.verbose('********** End announcing agent number (with error) **********')
        raise 
    
    fagi.verbose('End of announcing')

if __name__ == "__main__":
    main()

agid.register(main)
