from fastapi import FastAPI, Request, Security
from fastapi.middleware.cors import CORSMiddleware

from packages.backend.impl.module import RequestContext
from packages.backend.server.api.deps import _module, authorize
from packages.backend.server.api.main import api_router


app = FastAPI(
    #  Unfortunately, the Swagger will consider all routes to be private, even those we override as public.
    dependencies=[Security(authorize)],
)


app.include_router(api_router)


@app.middleware("http")
async def add_request_context_middleware(request: Request, call_next):
    request_context = RequestContext()
    with _module().request_context_provider().set(request_context):
        return await call_next(request)
