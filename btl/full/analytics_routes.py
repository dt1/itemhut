# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from full_route_utils import *

# analytics
@route("/analytics")
def analytics():
    return template("views/analytics/analytics", inv = inv)
