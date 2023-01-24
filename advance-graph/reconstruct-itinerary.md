# Reconstruct Itinerary

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      graph = {} # key is source value is list of destinations
      tickets_count = {}

      # Generate the graph
      for ticket in tickets:
        ticket_hash = ticket[0] + "+" + ticket[1]
        if not ticket_hash in tickets_count:
          tickets_count[ticket_hash] = 1
        else:
          tickets_count[ticket_hash] += 1

        if not ticket[0] in graph:
          graph[ticket[0]] = [ticket[1]]
        else:
          graph[ticket[0]].append(ticket[1])

        if not ticket[1] in graph:
          graph[ticket[1]] = []

      # Sort the destinations so we can find our lexical ordered output quickly
      for dest, src in tickets:
        graph[dest].sort()

      valid_routes = []

      def dfs(tickets_used, total_tickets, order):
        if total_tickets == len(tickets):
          valid_routes.append(order.copy())
          return True
        for destination in graph[order[-1]]:
          ticket = order[-1] + "+" + destination
          if tickets_used[ticket] < tickets_count[ticket]:
            tickets_used[ticket] += 1
            total_tickets += 1
            order.append(destination)
            if dfs(tickets_used, total_tickets, order):
              return True
            tickets_used[ticket] -= 1
            total_tickets -= 1
            order.pop()
        return False

      dfs({ ticket[0] + "+" + ticket[1] : 0 for ticket in tickets},0, ["JFK"])

      valid_routes_as_string = [",".join(list) for list in valid_routes]
      valid_routes_as_string.sort()
      if len(valid_routes_as_string):
        return valid_routes_as_string[0].split(",")
      else:
        return []
```
