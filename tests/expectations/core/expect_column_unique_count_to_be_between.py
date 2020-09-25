import pandas as pd
import numpy as np

from great_expectations import ExpectColumnUniqueValueCountToBeBetween
from great_expectations.core.batch import Batch
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.core.expectation_validation_result import (
    ExpectationValidationResult,
)
from great_expectations.execution_engine import PandasExecutionEngine
from great_expectations.expectations.core.expect_column_stdev_to_be_between import ExpectColumnStdevToBeBetween


def test_expect_column_unique_value_count_to_be_between_impl():
    df = pd.DataFrame({"a": [2, 17, 29, 29, 29,33]})
    expectationConfiguration = ExpectationConfiguration(
        expectation_type="expect_column_unique_value_count_to_be_between",
        kwargs={"column": "a", "min_value":2, "max_value":3},
    )
    expectation = ExpectColumnUniqueValueCountToBeBetween(expectationConfiguration)
    batch = Batch(data=df)
    result = expectation.validate(
        batches={"batch_id": batch}, execution_engine=PandasExecutionEngine()
    )
    assert result == ExpectationValidationResult(success=False,)