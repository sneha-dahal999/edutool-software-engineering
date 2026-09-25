# Sequence Design – Natural-Language Search

1. Registered user enters a natural-language query in the browser.
2. Browser sends the request to Flask.
3. Flask passes the query to the search/NLP service.
4. Search service prepares the query and requests matching data.
5. MongoDB returns matching book records.
6. Search service returns results to Flask.
7. Flask sends the results to the browser.
8. Browser displays the matching books.

The sequence is a proposed detailed design flow and should be refined if implementation decisions change.
