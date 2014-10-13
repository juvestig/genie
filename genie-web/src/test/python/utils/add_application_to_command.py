# #
#
#  Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
##

import sys

sys.path.append('../utils')

import eureka
import json
import restclient


def add_application_to_command(command_id, application_id):
    print "Adding Application [%s] to Command [%s] " % (application_id, command_id)

    # get the serviceUrl from the eureka client
    service_url = \
        eureka.EurekaClient().get_service_base_url() + '/genie/v2/config/commands/' + command_id + '/applications'
    print "Service Url isi %s" % service_url

    payload = json.dumps([{'id': application_id}])
    print payload
    print "\n"

    print restclient.post(service_url=service_url, payload=payload, content_type='application/json')

# driver method for all tests                
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: add_application_to_command command_id application_id"
        sys.exit(-1)

    add_application_to_command(sys.argv[1], sys.argv[2])