import asyncio


class Timer:
  def __init__(self, timeout, callback, arg):
    self._timeout = timeout
    self._callback = callback
    self.arg = arg
    self._task = asyncio.ensure_future(self._job())

  async def _job(self):
    await asyncio.sleep(self._timeout)
    await self._callback(self.arg)

  def cancel(self):
    self._task.cancel()

  