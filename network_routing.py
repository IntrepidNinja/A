# network_routing.py


def primecheck(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    for i in range(2, int(n**0.5) +1):
        if n%i==0:
            return 0
    return 1



"""
Sample test cases for the network routing optimization problem:
Select packets with prime-numbered IDs and top 10% priorities.
"""

# List of test cases (add more as needed)
test_cases = [
    {
        'packets': [
            {'packet_id': 2, 'priority': 50},
            {'packet_id': 3, 'priority': 90},
            {'packet_id': 4, 'priority': 80},
            {'packet_id': 5, 'priority': 95},
            {'packet_id': 6, 'priority': 60},
            {'packet_id': 7, 'priority': 99},
            {'packet_id': 8, 'priority': 30},
            {'packet_id': 11, 'priority': 100},
            {'packet_id': 13, 'priority': 10},
            {'packet_id': 17, 'priority': 85}
        ],
        'expected': [
            {'packet_id': 11, 'priority': 100}
        ]
    },
    {
        'packets': [
            {'packet_id': 4, 'priority': 10},
            {'packet_id': 6, 'priority': 20},
            {'packet_id': 8, 'priority': 30},
            {'packet_id': 9, 'priority': 40}
        ],
        'expected': []
    }
    # Add more test cases here as needed
]

# Solution for selecting packets with prime-numbered IDs and top 10% priorities
def select_priority_packets(packets):
    if not packets:
        return []
    priorities = sorted([p['priority'] for p in packets], reverse=True)
    top_n = max(1, len(priorities) // 10)
    threshold = priorities[top_n - 1]
    return [p for p in packets if primecheck(p['packet_id'])==1 and p['priority'] >= threshold]

# Run and print results for all test cases
for idx, case in enumerate(test_cases, 1):
    result = select_priority_packets(case['packets'])
    print(f'Test case {idx} result:', result)
    print(f'Test case {idx} passed:', result == case['expected'])




