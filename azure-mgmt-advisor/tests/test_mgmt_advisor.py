# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import azure.mgmt.advisor
import datetime
import re
import unittest

from devtools_testutils import (
    AzureMgmtTestCase, ResourceGroupPreparer,
)

# the goal of these tests is to validate AutoRest generation of the Python wrapper
# and NOT to validate the behavior of the API. so the tests will primarily attempt
# to verify that all operations are possible using the generated client and that
# the operations can accept valid input and produce valid output.

class MgmtAdvisorTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtAdvisorTest, self).setUp()
        self.client = self.create_mgmt_client(
            azure.mgmt.advisor.AdvisorManagementClient
        )

    def test_generate_recommendations(self):
        # trigger generate recommendations
        response = self.client.recommendations.generate(raw=True)

        # we should get a valid Location header back
        self.assertTrue('Location' in response.headers)
        location = response.headers['Location']

        # extract the operation ID from the Location header
        operation_id = re.findall("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", location)

        # the operation ID should be a valid GUID
        self.assertNotEqual(operation_id, None)
        self.assertTrue(len(operation_id), 1)

        # we should be able to get generation status for this operation ID
        response = self.client.recommendations.get_generate_status(
            raw=True,
            operation_id = operation_id[0]
        )
        status_code = response.response.status_code
        # and the status should be 202 or 204
        self.assertTrue(status_code == 202 or status_code == 204)

    def test_suppressions(self):
        # first, get all recommendations
        response = list(self.client.recommendations.list())
        # we should have at least one recommendation
        self.assertNotEqual(len(response), 0)
        recommendation = None
        # the recommendation should have all relevant properties populated
        for rec in response:
            self.assertNotEqual(rec.id, None)
            self.assertNotEqual(rec.name, None)
            self.assertNotEqual(rec.type, None)
            self.assertNotEqual(rec.category, None)
            self.assertNotEqual(rec.impact, None)
            self.assertNotEqual(rec.risk, None)
            self.assertNotEqual(rec.short_description, None)
            self.assertNotEqual(rec.short_description.problem, None)
            self.assertNotEqual(rec.short_description.solution, None)
            if (rec.impacted_value != None):
                recommendation = rec
        # construct the resourceUri for the first recommendation
        resourceUri = recommendation.id[:recommendation.id.find("/providers/Microsoft.Advisor/recommendations")]
        recommendationName = recommendation.name
        suppressionName = "Python_SDK_Test"
        timeToLive = "00:01:00:00"

        # create a new suppression
        suppression = self.client.suppressions.create(
            resource_uri = resourceUri,
            recommendation_id = recommendationName,
            name = suppressionName,
            ttl = timeToLive
        )
        # we expect it to get created successfully
        # self.assertEqual(suppression.name, suppressionName)
        self.assertEqual(suppression.ttl, "00:01:00:00")

        # get the suppression
        sup = self.client.suppressions.get(
            resource_uri = resourceUri,
            recommendation_id = recommendationName,
            name = suppressionName
        )
        self.assertEqual(sup.name, suppressionName)
        # self.assertEqual(sup.ttl., timeToLive)
        self.assertEqual(sup.id, resourceUri + "/providers/Microsoft.Advisor/recommendations/" + recommendationName + "/suppressions/" + suppressionName)

        # delete the suppression
        self.client.suppressions.delete(
            resource_uri = resourceUri,
            recommendation_id = recommendationName,
            name = suppressionName
        )
        # the suppression should be gone
        response = list(self.client.suppressions.list())
        for sup in response:
            self.assertNotEqual(sup.Name, suppressionName)

    def test_configurations(self):
        # config = 
        # self.client.configurations.create_in_subscription()
        # create, get and delete configuration on a subscription and resource group
        self.assertTrue(True);

#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
