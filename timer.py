import asyncio


class Timer:
  # TODO make args**
  def __init__(self, timeout, callback, arg1, arg2):
    self._timeout = timeout
    self._callback = callback
    self.arg1 = arg1
    self.arg2 = arg2
    self._task = asyncio.ensure_future(self._job())

  async def _job(self):
    await asyncio.sleep(self._timeout)
    await self._callback(self.arg1, self.arg2)

  def cancel(self):
    self._task.cancel()

  