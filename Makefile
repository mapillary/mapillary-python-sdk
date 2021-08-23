# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)

style:
	black src/mapillary && flake8 src/mapillary

test:
	@ pytest --log-cli-level=20
