# Transcribe Streaming

## Client

::: aws_sdk_transcribe_streaming.client.TranscribeStreamingClient
    options:
        merge_init_into_class: true
        members: false
        heading_level: 3

### Initialization

```python

from aws_sdk_transcribe_streaming.client import TranscribeStreamingClient

# Initialize the client
client = TranscribeStreamingClient()

```

## Config

::: aws_sdk_transcribe_streaming.config.Config
    options:
        heading_level: 3

## Operations

- [get_medical_scribe_stream](operations/get_medical_scribe_stream.md)

- [start_call_analytics_stream_transcription](operations/start_call_analytics_stream_transcription.md)

- [start_medical_scribe_stream](operations/start_medical_scribe_stream.md)

- [start_medical_stream_transcription](operations/start_medical_stream_transcription.md)

- [start_stream_transcription](operations/start_stream_transcription.md)

## Models

- [Alternative](models/Alternative.md)

- [AudioEvent](models/AudioEvent.md)

- [AudioStream](models/AudioStream.md)

- [AudioStreamAudioEvent](models/AudioStreamAudioEvent.md)

- [AudioStreamConfigurationEvent](models/AudioStreamConfigurationEvent.md)

- [AudioStreamUnknown](models/AudioStreamUnknown.md)

- [BadRequestException](models/BadRequestException.md)

- [CallAnalyticsEntity](models/CallAnalyticsEntity.md)

- [CallAnalyticsItem](models/CallAnalyticsItem.md)

- [CallAnalyticsLanguageWithScore](models/CallAnalyticsLanguageWithScore.md)

- [CallAnalyticsTranscriptResultStream](models/CallAnalyticsTranscriptResultStream.md)

- [CallAnalyticsTranscriptResultStreamBadRequestException](models/CallAnalyticsTranscriptResultStreamBadRequestException.md)

- [CallAnalyticsTranscriptResultStreamCategoryEvent](models/CallAnalyticsTranscriptResultStreamCategoryEvent.md)

- [CallAnalyticsTranscriptResultStreamConflictException](models/CallAnalyticsTranscriptResultStreamConflictException.md)

- [CallAnalyticsTranscriptResultStreamInternalFailureException](models/CallAnalyticsTranscriptResultStreamInternalFailureException.md)

- [CallAnalyticsTranscriptResultStreamLimitExceededException](models/CallAnalyticsTranscriptResultStreamLimitExceededException.md)

- [CallAnalyticsTranscriptResultStreamServiceUnavailableException](models/CallAnalyticsTranscriptResultStreamServiceUnavailableException.md)

- [CallAnalyticsTranscriptResultStreamUnknown](models/CallAnalyticsTranscriptResultStreamUnknown.md)

- [CallAnalyticsTranscriptResultStreamUtteranceEvent](models/CallAnalyticsTranscriptResultStreamUtteranceEvent.md)

- [CategoryEvent](models/CategoryEvent.md)

- [ChannelDefinition](models/ChannelDefinition.md)

- [CharacterOffsets](models/CharacterOffsets.md)

- [ClinicalNoteGenerationResult](models/ClinicalNoteGenerationResult.md)

- [ClinicalNoteGenerationSettings](models/ClinicalNoteGenerationSettings.md)

- [ConfigurationEvent](models/ConfigurationEvent.md)

- [ConflictException](models/ConflictException.md)

- [Entity](models/Entity.md)

- [InternalFailureException](models/InternalFailureException.md)

- [IssueDetected](models/IssueDetected.md)

- [Item](models/Item.md)

- [LanguageWithScore](models/LanguageWithScore.md)

- [LimitExceededException](models/LimitExceededException.md)

- [MedicalAlternative](models/MedicalAlternative.md)

- [MedicalEntity](models/MedicalEntity.md)

- [MedicalItem](models/MedicalItem.md)

- [MedicalResult](models/MedicalResult.md)

- [MedicalScribeAudioEvent](models/MedicalScribeAudioEvent.md)

- [MedicalScribeChannelDefinition](models/MedicalScribeChannelDefinition.md)

- [MedicalScribeConfigurationEvent](models/MedicalScribeConfigurationEvent.md)

- [MedicalScribeContext](models/MedicalScribeContext.md)

- [MedicalScribeEncryptionSettings](models/MedicalScribeEncryptionSettings.md)

- [MedicalScribeInputStream](models/MedicalScribeInputStream.md)

- [MedicalScribeInputStreamAudioEvent](models/MedicalScribeInputStreamAudioEvent.md)

- [MedicalScribeInputStreamConfigurationEvent](models/MedicalScribeInputStreamConfigurationEvent.md)

- [MedicalScribeInputStreamSessionControlEvent](models/MedicalScribeInputStreamSessionControlEvent.md)

- [MedicalScribeInputStreamUnknown](models/MedicalScribeInputStreamUnknown.md)

- [MedicalScribePatientContext](models/MedicalScribePatientContext.md)

- [MedicalScribePostStreamAnalyticsResult](models/MedicalScribePostStreamAnalyticsResult.md)

- [MedicalScribePostStreamAnalyticsSettings](models/MedicalScribePostStreamAnalyticsSettings.md)

- [MedicalScribeResultStream](models/MedicalScribeResultStream.md)

- [MedicalScribeResultStreamBadRequestException](models/MedicalScribeResultStreamBadRequestException.md)

- [MedicalScribeResultStreamConflictException](models/MedicalScribeResultStreamConflictException.md)

- [MedicalScribeResultStreamInternalFailureException](models/MedicalScribeResultStreamInternalFailureException.md)

- [MedicalScribeResultStreamLimitExceededException](models/MedicalScribeResultStreamLimitExceededException.md)

- [MedicalScribeResultStreamServiceUnavailableException](models/MedicalScribeResultStreamServiceUnavailableException.md)

- [MedicalScribeResultStreamTranscriptEvent](models/MedicalScribeResultStreamTranscriptEvent.md)

- [MedicalScribeResultStreamUnknown](models/MedicalScribeResultStreamUnknown.md)

- [MedicalScribeSessionControlEvent](models/MedicalScribeSessionControlEvent.md)

- [MedicalScribeStreamDetails](models/MedicalScribeStreamDetails.md)

- [MedicalScribeTranscriptEvent](models/MedicalScribeTranscriptEvent.md)

- [MedicalScribeTranscriptItem](models/MedicalScribeTranscriptItem.md)

- [MedicalScribeTranscriptSegment](models/MedicalScribeTranscriptSegment.md)

- [MedicalTranscript](models/MedicalTranscript.md)

- [MedicalTranscriptEvent](models/MedicalTranscriptEvent.md)

- [MedicalTranscriptResultStream](models/MedicalTranscriptResultStream.md)

- [MedicalTranscriptResultStreamBadRequestException](models/MedicalTranscriptResultStreamBadRequestException.md)

- [MedicalTranscriptResultStreamConflictException](models/MedicalTranscriptResultStreamConflictException.md)

- [MedicalTranscriptResultStreamInternalFailureException](models/MedicalTranscriptResultStreamInternalFailureException.md)

- [MedicalTranscriptResultStreamLimitExceededException](models/MedicalTranscriptResultStreamLimitExceededException.md)

- [MedicalTranscriptResultStreamServiceUnavailableException](models/MedicalTranscriptResultStreamServiceUnavailableException.md)

- [MedicalTranscriptResultStreamTranscriptEvent](models/MedicalTranscriptResultStreamTranscriptEvent.md)

- [MedicalTranscriptResultStreamUnknown](models/MedicalTranscriptResultStreamUnknown.md)

- [PointsOfInterest](models/PointsOfInterest.md)

- [PostCallAnalyticsSettings](models/PostCallAnalyticsSettings.md)

- [ResourceNotFoundException](models/ResourceNotFoundException.md)

- [Result](models/Result.md)

- [ServiceUnavailableException](models/ServiceUnavailableException.md)

- [TimestampRange](models/TimestampRange.md)

- [Transcript](models/Transcript.md)

- [TranscriptEvent](models/TranscriptEvent.md)

- [TranscriptResultStream](models/TranscriptResultStream.md)

- [TranscriptResultStreamBadRequestException](models/TranscriptResultStreamBadRequestException.md)

- [TranscriptResultStreamConflictException](models/TranscriptResultStreamConflictException.md)

- [TranscriptResultStreamInternalFailureException](models/TranscriptResultStreamInternalFailureException.md)

- [TranscriptResultStreamLimitExceededException](models/TranscriptResultStreamLimitExceededException.md)

- [TranscriptResultStreamServiceUnavailableException](models/TranscriptResultStreamServiceUnavailableException.md)

- [TranscriptResultStreamTranscriptEvent](models/TranscriptResultStreamTranscriptEvent.md)

- [TranscriptResultStreamUnknown](models/TranscriptResultStreamUnknown.md)

- [UtteranceEvent](models/UtteranceEvent.md)
