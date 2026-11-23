1. **PROBLEM** : Normally, each request goes to the language model. That takes time and uses GPU resources. A semantic cache tries to recognize when a new request is close enough in meaning to one it has already answered, then returns the saved answer 
2. MAIN IDEA : A small service that
	1. Receives a user prompt.
	2. Creates an embedding for it.
	3. Searches previously answered prompts for a close match
	4. Returns the cached answer when it’s safe to do so
	5. Calls the language model when there’s no suitable match, then saves the new prompt and answer.
3. STEPS : 
    1. **Python + FastAPI** for the service API and rapid iteration
    2. **PostgreSQL + pgvector** for cache entries, metadata, and vector search in one place. pgvector supports exact search and approximate indexes, so we can start with exact matches and add indexing as the cache grows 
    3. **A swappable embedding interface**, so we can begin with one embedding provider and change it later without rewriting the cache. If we use OpenAI embeddings, the current API supports choosing output dimensions
    4. **Redis later**, only if we need a separate fast exact-match layer or other in-memory operations. It supports vector search too, but I’d keep the first version simpler and avoid operating two stores