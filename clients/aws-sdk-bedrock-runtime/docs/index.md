# Bedrock Runtime

## Client

::: aws_sdk_bedrock_runtime.client.BedrockRuntimeClient
    options:
        merge_init_into_class: true
        members: false
        heading_level: 3

### Initialization

```python

from aws_sdk_bedrock_runtime.client import BedrockRuntimeClient

# Initialize the client
client = BedrockRuntimeClient()

```

## Config

::: aws_sdk_bedrock_runtime.config.Config
    options:
        heading_level: 3

## Operations

- [apply_guardrail](operations/apply_guardrail.md)

- [converse](operations/converse.md)

- [converse_stream](operations/converse_stream.md)

- [count_tokens](operations/count_tokens.md)

- [get_async_invoke](operations/get_async_invoke.md)

- [invoke_model](operations/invoke_model.md)

- [invoke_model_with_bidirectional_stream](operations/invoke_model_with_bidirectional_stream.md)

- [invoke_model_with_response_stream](operations/invoke_model_with_response_stream.md)

- [list_async_invokes](operations/list_async_invokes.md)

- [start_async_invoke](operations/start_async_invoke.md)

## Models

- [AccessDeniedException](models/AccessDeniedException.md)

- [AnyToolChoice](models/AnyToolChoice.md)

- [AsyncInvokeOutputDataConfig](models/AsyncInvokeOutputDataConfig.md)

- [AsyncInvokeOutputDataConfigS3OutputDataConfig](models/AsyncInvokeOutputDataConfigS3OutputDataConfig.md)

- [AsyncInvokeOutputDataConfigUnknown](models/AsyncInvokeOutputDataConfigUnknown.md)

- [AsyncInvokeS3OutputDataConfig](models/AsyncInvokeS3OutputDataConfig.md)

- [AsyncInvokeSummary](models/AsyncInvokeSummary.md)

- [AutoToolChoice](models/AutoToolChoice.md)

- [BidirectionalInputPayloadPart](models/BidirectionalInputPayloadPart.md)

- [BidirectionalOutputPayloadPart](models/BidirectionalOutputPayloadPart.md)

- [CachePointBlock](models/CachePointBlock.md)

- [Citation](models/Citation.md)

- [CitationGeneratedContent](models/CitationGeneratedContent.md)

- [CitationGeneratedContentText](models/CitationGeneratedContentText.md)

- [CitationGeneratedContentUnknown](models/CitationGeneratedContentUnknown.md)

- [CitationLocation](models/CitationLocation.md)

- [CitationLocationDocumentChar](models/CitationLocationDocumentChar.md)

- [CitationLocationDocumentChunk](models/CitationLocationDocumentChunk.md)

- [CitationLocationDocumentPage](models/CitationLocationDocumentPage.md)

- [CitationLocationUnknown](models/CitationLocationUnknown.md)

- [CitationSourceContent](models/CitationSourceContent.md)

- [CitationSourceContentDelta](models/CitationSourceContentDelta.md)

- [CitationSourceContentText](models/CitationSourceContentText.md)

- [CitationSourceContentUnknown](models/CitationSourceContentUnknown.md)

- [CitationsConfig](models/CitationsConfig.md)

- [CitationsContentBlock](models/CitationsContentBlock.md)

- [CitationsDelta](models/CitationsDelta.md)

- [ConflictException](models/ConflictException.md)

- [ContentBlock](models/ContentBlock.md)

- [ContentBlockCachePoint](models/ContentBlockCachePoint.md)

- [ContentBlockCitationsContent](models/ContentBlockCitationsContent.md)

- [ContentBlockDelta](models/ContentBlockDelta.md)

- [ContentBlockDeltaCitation](models/ContentBlockDeltaCitation.md)

- [ContentBlockDeltaEvent](models/ContentBlockDeltaEvent.md)

- [ContentBlockDeltaReasoningContent](models/ContentBlockDeltaReasoningContent.md)

- [ContentBlockDeltaText](models/ContentBlockDeltaText.md)

- [ContentBlockDeltaToolUse](models/ContentBlockDeltaToolUse.md)

- [ContentBlockDeltaUnknown](models/ContentBlockDeltaUnknown.md)

- [ContentBlockDocument](models/ContentBlockDocument.md)

- [ContentBlockGuardContent](models/ContentBlockGuardContent.md)

- [ContentBlockImage](models/ContentBlockImage.md)

- [ContentBlockReasoningContent](models/ContentBlockReasoningContent.md)

- [ContentBlockStart](models/ContentBlockStart.md)

- [ContentBlockStartEvent](models/ContentBlockStartEvent.md)

- [ContentBlockStartToolUse](models/ContentBlockStartToolUse.md)

- [ContentBlockStartUnknown](models/ContentBlockStartUnknown.md)

- [ContentBlockStopEvent](models/ContentBlockStopEvent.md)

- [ContentBlockText](models/ContentBlockText.md)

- [ContentBlockToolResult](models/ContentBlockToolResult.md)

- [ContentBlockToolUse](models/ContentBlockToolUse.md)

- [ContentBlockUnknown](models/ContentBlockUnknown.md)

- [ContentBlockVideo](models/ContentBlockVideo.md)

- [ConverseMetrics](models/ConverseMetrics.md)

- [ConverseOutput](models/ConverseOutput.md)

- [ConverseOutputMessage](models/ConverseOutputMessage.md)

- [ConverseOutputUnknown](models/ConverseOutputUnknown.md)

- [ConverseStreamMetadataEvent](models/ConverseStreamMetadataEvent.md)

- [ConverseStreamMetrics](models/ConverseStreamMetrics.md)

- [ConverseStreamOutput](models/ConverseStreamOutput.md)

- [ConverseStreamOutputContentBlockDelta](models/ConverseStreamOutputContentBlockDelta.md)

- [ConverseStreamOutputContentBlockStart](models/ConverseStreamOutputContentBlockStart.md)

- [ConverseStreamOutputContentBlockStop](models/ConverseStreamOutputContentBlockStop.md)

- [ConverseStreamOutputInternalServerException](models/ConverseStreamOutputInternalServerException.md)

- [ConverseStreamOutputMessageStart](models/ConverseStreamOutputMessageStart.md)

- [ConverseStreamOutputMessageStop](models/ConverseStreamOutputMessageStop.md)

- [ConverseStreamOutputMetadata](models/ConverseStreamOutputMetadata.md)

- [ConverseStreamOutputModelStreamErrorException](models/ConverseStreamOutputModelStreamErrorException.md)

- [ConverseStreamOutputServiceUnavailableException](models/ConverseStreamOutputServiceUnavailableException.md)

- [ConverseStreamOutputThrottlingException](models/ConverseStreamOutputThrottlingException.md)

- [ConverseStreamOutputUnknown](models/ConverseStreamOutputUnknown.md)

- [ConverseStreamOutputValidationException](models/ConverseStreamOutputValidationException.md)

- [ConverseStreamTrace](models/ConverseStreamTrace.md)

- [ConverseTokensRequest](models/ConverseTokensRequest.md)

- [ConverseTrace](models/ConverseTrace.md)

- [CountTokensInput](models/CountTokensInput.md)

- [CountTokensInputConverse](models/CountTokensInputConverse.md)

- [CountTokensInputInvokeModel](models/CountTokensInputInvokeModel.md)

- [CountTokensInputUnknown](models/CountTokensInputUnknown.md)

- [DocumentBlock](models/DocumentBlock.md)

- [DocumentCharLocation](models/DocumentCharLocation.md)

- [DocumentChunkLocation](models/DocumentChunkLocation.md)

- [DocumentContentBlock](models/DocumentContentBlock.md)

- [DocumentContentBlockText](models/DocumentContentBlockText.md)

- [DocumentContentBlockUnknown](models/DocumentContentBlockUnknown.md)

- [DocumentPageLocation](models/DocumentPageLocation.md)

- [DocumentSource](models/DocumentSource.md)

- [DocumentSourceBytes](models/DocumentSourceBytes.md)

- [DocumentSourceContent](models/DocumentSourceContent.md)

- [DocumentSourceS3Location](models/DocumentSourceS3Location.md)

- [DocumentSourceText](models/DocumentSourceText.md)

- [DocumentSourceUnknown](models/DocumentSourceUnknown.md)

- [GuardrailAssessment](models/GuardrailAssessment.md)

- [GuardrailAutomatedReasoningFinding](models/GuardrailAutomatedReasoningFinding.md)

- [GuardrailAutomatedReasoningFindingImpossible](models/GuardrailAutomatedReasoningFindingImpossible.md)

- [GuardrailAutomatedReasoningFindingInvalid](models/GuardrailAutomatedReasoningFindingInvalid.md)

- [GuardrailAutomatedReasoningFindingNoTranslations](models/GuardrailAutomatedReasoningFindingNoTranslations.md)

- [GuardrailAutomatedReasoningFindingSatisfiable](models/GuardrailAutomatedReasoningFindingSatisfiable.md)

- [GuardrailAutomatedReasoningFindingTooComplex](models/GuardrailAutomatedReasoningFindingTooComplex.md)

- [GuardrailAutomatedReasoningFindingTranslationAmbiguous](models/GuardrailAutomatedReasoningFindingTranslationAmbiguous.md)

- [GuardrailAutomatedReasoningFindingUnknown](models/GuardrailAutomatedReasoningFindingUnknown.md)

- [GuardrailAutomatedReasoningFindingValid](models/GuardrailAutomatedReasoningFindingValid.md)

- [GuardrailAutomatedReasoningImpossibleFinding](models/GuardrailAutomatedReasoningImpossibleFinding.md)

- [GuardrailAutomatedReasoningInputTextReference](models/GuardrailAutomatedReasoningInputTextReference.md)

- [GuardrailAutomatedReasoningInvalidFinding](models/GuardrailAutomatedReasoningInvalidFinding.md)

- [GuardrailAutomatedReasoningLogicWarning](models/GuardrailAutomatedReasoningLogicWarning.md)

- [GuardrailAutomatedReasoningNoTranslationsFinding](models/GuardrailAutomatedReasoningNoTranslationsFinding.md)

- [GuardrailAutomatedReasoningPolicyAssessment](models/GuardrailAutomatedReasoningPolicyAssessment.md)

- [GuardrailAutomatedReasoningRule](models/GuardrailAutomatedReasoningRule.md)

- [GuardrailAutomatedReasoningSatisfiableFinding](models/GuardrailAutomatedReasoningSatisfiableFinding.md)

- [GuardrailAutomatedReasoningScenario](models/GuardrailAutomatedReasoningScenario.md)

- [GuardrailAutomatedReasoningStatement](models/GuardrailAutomatedReasoningStatement.md)

- [GuardrailAutomatedReasoningTooComplexFinding](models/GuardrailAutomatedReasoningTooComplexFinding.md)

- [GuardrailAutomatedReasoningTranslation](models/GuardrailAutomatedReasoningTranslation.md)

- [GuardrailAutomatedReasoningTranslationAmbiguousFinding](models/GuardrailAutomatedReasoningTranslationAmbiguousFinding.md)

- [GuardrailAutomatedReasoningTranslationOption](models/GuardrailAutomatedReasoningTranslationOption.md)

- [GuardrailAutomatedReasoningValidFinding](models/GuardrailAutomatedReasoningValidFinding.md)

- [GuardrailConfiguration](models/GuardrailConfiguration.md)

- [GuardrailContentBlock](models/GuardrailContentBlock.md)

- [GuardrailContentBlockImage](models/GuardrailContentBlockImage.md)

- [GuardrailContentBlockText](models/GuardrailContentBlockText.md)

- [GuardrailContentBlockUnknown](models/GuardrailContentBlockUnknown.md)

- [GuardrailContentFilter](models/GuardrailContentFilter.md)

- [GuardrailContentPolicyAssessment](models/GuardrailContentPolicyAssessment.md)

- [GuardrailContextualGroundingFilter](models/GuardrailContextualGroundingFilter.md)

- [GuardrailContextualGroundingPolicyAssessment](models/GuardrailContextualGroundingPolicyAssessment.md)

- [GuardrailConverseContentBlock](models/GuardrailConverseContentBlock.md)

- [GuardrailConverseContentBlockImage](models/GuardrailConverseContentBlockImage.md)

- [GuardrailConverseContentBlockText](models/GuardrailConverseContentBlockText.md)

- [GuardrailConverseContentBlockUnknown](models/GuardrailConverseContentBlockUnknown.md)

- [GuardrailConverseImageBlock](models/GuardrailConverseImageBlock.md)

- [GuardrailConverseImageSource](models/GuardrailConverseImageSource.md)

- [GuardrailConverseImageSourceBytes](models/GuardrailConverseImageSourceBytes.md)

- [GuardrailConverseImageSourceUnknown](models/GuardrailConverseImageSourceUnknown.md)

- [GuardrailConverseTextBlock](models/GuardrailConverseTextBlock.md)

- [GuardrailCoverage](models/GuardrailCoverage.md)

- [GuardrailCustomWord](models/GuardrailCustomWord.md)

- [GuardrailImageBlock](models/GuardrailImageBlock.md)

- [GuardrailImageCoverage](models/GuardrailImageCoverage.md)

- [GuardrailImageSource](models/GuardrailImageSource.md)

- [GuardrailImageSourceBytes](models/GuardrailImageSourceBytes.md)

- [GuardrailImageSourceUnknown](models/GuardrailImageSourceUnknown.md)

- [GuardrailInvocationMetrics](models/GuardrailInvocationMetrics.md)

- [GuardrailManagedWord](models/GuardrailManagedWord.md)

- [GuardrailOutputContent](models/GuardrailOutputContent.md)

- [GuardrailPiiEntityFilter](models/GuardrailPiiEntityFilter.md)

- [GuardrailRegexFilter](models/GuardrailRegexFilter.md)

- [GuardrailSensitiveInformationPolicyAssessment](models/GuardrailSensitiveInformationPolicyAssessment.md)

- [GuardrailStreamConfiguration](models/GuardrailStreamConfiguration.md)

- [GuardrailTextBlock](models/GuardrailTextBlock.md)

- [GuardrailTextCharactersCoverage](models/GuardrailTextCharactersCoverage.md)

- [GuardrailTopic](models/GuardrailTopic.md)

- [GuardrailTopicPolicyAssessment](models/GuardrailTopicPolicyAssessment.md)

- [GuardrailTraceAssessment](models/GuardrailTraceAssessment.md)

- [GuardrailUsage](models/GuardrailUsage.md)

- [GuardrailWordPolicyAssessment](models/GuardrailWordPolicyAssessment.md)

- [ImageBlock](models/ImageBlock.md)

- [ImageSource](models/ImageSource.md)

- [ImageSourceBytes](models/ImageSourceBytes.md)

- [ImageSourceS3Location](models/ImageSourceS3Location.md)

- [ImageSourceUnknown](models/ImageSourceUnknown.md)

- [InferenceConfiguration](models/InferenceConfiguration.md)

- [InternalServerException](models/InternalServerException.md)

- [InvokeModelTokensRequest](models/InvokeModelTokensRequest.md)

- [InvokeModelWithBidirectionalStreamInput](models/InvokeModelWithBidirectionalStreamInput.md)

- [InvokeModelWithBidirectionalStreamInputChunk](models/InvokeModelWithBidirectionalStreamInputChunk.md)

- [InvokeModelWithBidirectionalStreamInputUnknown](models/InvokeModelWithBidirectionalStreamInputUnknown.md)

- [InvokeModelWithBidirectionalStreamOutput](models/InvokeModelWithBidirectionalStreamOutput.md)

- [InvokeModelWithBidirectionalStreamOutputChunk](models/InvokeModelWithBidirectionalStreamOutputChunk.md)

- [InvokeModelWithBidirectionalStreamOutputInternalServerException](models/InvokeModelWithBidirectionalStreamOutputInternalServerException.md)

- [InvokeModelWithBidirectionalStreamOutputModelStreamErrorException](models/InvokeModelWithBidirectionalStreamOutputModelStreamErrorException.md)

- [InvokeModelWithBidirectionalStreamOutputModelTimeoutException](models/InvokeModelWithBidirectionalStreamOutputModelTimeoutException.md)

- [InvokeModelWithBidirectionalStreamOutputServiceUnavailableException](models/InvokeModelWithBidirectionalStreamOutputServiceUnavailableException.md)

- [InvokeModelWithBidirectionalStreamOutputThrottlingException](models/InvokeModelWithBidirectionalStreamOutputThrottlingException.md)

- [InvokeModelWithBidirectionalStreamOutputUnknown](models/InvokeModelWithBidirectionalStreamOutputUnknown.md)

- [InvokeModelWithBidirectionalStreamOutputValidationException](models/InvokeModelWithBidirectionalStreamOutputValidationException.md)

- [Message](models/Message.md)

- [MessageStartEvent](models/MessageStartEvent.md)

- [MessageStopEvent](models/MessageStopEvent.md)

- [ModelErrorException](models/ModelErrorException.md)

- [ModelNotReadyException](models/ModelNotReadyException.md)

- [ModelStreamErrorException](models/ModelStreamErrorException.md)

- [ModelTimeoutException](models/ModelTimeoutException.md)

- [PayloadPart](models/PayloadPart.md)

- [PerformanceConfiguration](models/PerformanceConfiguration.md)

- [PromptRouterTrace](models/PromptRouterTrace.md)

- [PromptVariableValues](models/PromptVariableValues.md)

- [PromptVariableValuesText](models/PromptVariableValuesText.md)

- [PromptVariableValuesUnknown](models/PromptVariableValuesUnknown.md)

- [ReasoningContentBlock](models/ReasoningContentBlock.md)

- [ReasoningContentBlockDelta](models/ReasoningContentBlockDelta.md)

- [ReasoningContentBlockDeltaRedactedContent](models/ReasoningContentBlockDeltaRedactedContent.md)

- [ReasoningContentBlockDeltaSignature](models/ReasoningContentBlockDeltaSignature.md)

- [ReasoningContentBlockDeltaText](models/ReasoningContentBlockDeltaText.md)

- [ReasoningContentBlockDeltaUnknown](models/ReasoningContentBlockDeltaUnknown.md)

- [ReasoningContentBlockReasoningText](models/ReasoningContentBlockReasoningText.md)

- [ReasoningContentBlockRedactedContent](models/ReasoningContentBlockRedactedContent.md)

- [ReasoningContentBlockUnknown](models/ReasoningContentBlockUnknown.md)

- [ReasoningTextBlock](models/ReasoningTextBlock.md)

- [ResourceNotFoundException](models/ResourceNotFoundException.md)

- [ResponseStream](models/ResponseStream.md)

- [ResponseStreamChunk](models/ResponseStreamChunk.md)

- [ResponseStreamInternalServerException](models/ResponseStreamInternalServerException.md)

- [ResponseStreamModelStreamErrorException](models/ResponseStreamModelStreamErrorException.md)

- [ResponseStreamModelTimeoutException](models/ResponseStreamModelTimeoutException.md)

- [ResponseStreamServiceUnavailableException](models/ResponseStreamServiceUnavailableException.md)

- [ResponseStreamThrottlingException](models/ResponseStreamThrottlingException.md)

- [ResponseStreamUnknown](models/ResponseStreamUnknown.md)

- [ResponseStreamValidationException](models/ResponseStreamValidationException.md)

- [S3Location](models/S3Location.md)

- [ServiceQuotaExceededException](models/ServiceQuotaExceededException.md)

- [ServiceUnavailableException](models/ServiceUnavailableException.md)

- [SpecificToolChoice](models/SpecificToolChoice.md)

- [SystemContentBlock](models/SystemContentBlock.md)

- [SystemContentBlockCachePoint](models/SystemContentBlockCachePoint.md)

- [SystemContentBlockGuardContent](models/SystemContentBlockGuardContent.md)

- [SystemContentBlockText](models/SystemContentBlockText.md)

- [SystemContentBlockUnknown](models/SystemContentBlockUnknown.md)

- [Tag](models/Tag.md)

- [ThrottlingException](models/ThrottlingException.md)

- [TokenUsage](models/TokenUsage.md)

- [Tool](models/Tool.md)

- [ToolCachePoint](models/ToolCachePoint.md)

- [ToolChoice](models/ToolChoice.md)

- [ToolChoiceAny](models/ToolChoiceAny.md)

- [ToolChoiceAuto](models/ToolChoiceAuto.md)

- [ToolChoiceTool](models/ToolChoiceTool.md)

- [ToolChoiceUnknown](models/ToolChoiceUnknown.md)

- [ToolConfiguration](models/ToolConfiguration.md)

- [ToolInputSchema](models/ToolInputSchema.md)

- [ToolInputSchemaJson](models/ToolInputSchemaJson.md)

- [ToolInputSchemaUnknown](models/ToolInputSchemaUnknown.md)

- [ToolResultBlock](models/ToolResultBlock.md)

- [ToolResultContentBlock](models/ToolResultContentBlock.md)

- [ToolResultContentBlockDocument](models/ToolResultContentBlockDocument.md)

- [ToolResultContentBlockImage](models/ToolResultContentBlockImage.md)

- [ToolResultContentBlockJson](models/ToolResultContentBlockJson.md)

- [ToolResultContentBlockText](models/ToolResultContentBlockText.md)

- [ToolResultContentBlockUnknown](models/ToolResultContentBlockUnknown.md)

- [ToolResultContentBlockVideo](models/ToolResultContentBlockVideo.md)

- [ToolSpecification](models/ToolSpecification.md)

- [ToolToolSpec](models/ToolToolSpec.md)

- [ToolUnknown](models/ToolUnknown.md)

- [ToolUseBlock](models/ToolUseBlock.md)

- [ToolUseBlockDelta](models/ToolUseBlockDelta.md)

- [ToolUseBlockStart](models/ToolUseBlockStart.md)

- [ValidationException](models/ValidationException.md)

- [VideoBlock](models/VideoBlock.md)

- [VideoSource](models/VideoSource.md)

- [VideoSourceBytes](models/VideoSourceBytes.md)

- [VideoSourceS3Location](models/VideoSourceS3Location.md)

- [VideoSourceUnknown](models/VideoSourceUnknown.md)
