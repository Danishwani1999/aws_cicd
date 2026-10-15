#!/bin/bash
# Give the app a few seconds to boot, then call the health endpoint.
for i in 1 2 3 4 5; do
  if curl -fs http://localhost/health > /dev/null; then
    echo "app is healthy"
    exit 0
  fi
  sleep 3
done
echo "health check failed"
exit 1
