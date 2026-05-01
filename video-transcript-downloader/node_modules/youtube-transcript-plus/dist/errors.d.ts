export declare class YoutubeTranscriptTooManyRequestError extends Error {
    constructor();
}
export declare class YoutubeTranscriptVideoUnavailableError extends Error {
    constructor(videoId: string);
}
export declare class YoutubeTranscriptDisabledError extends Error {
    constructor(videoId: string);
}
export declare class YoutubeTranscriptNotAvailableError extends Error {
    constructor(videoId: string);
}
export declare class YoutubeTranscriptNotAvailableLanguageError extends Error {
    constructor(lang: string, availableLangs: string[], videoId: string);
}
export declare class YoutubeTranscriptInvalidVideoIdError extends Error {
    constructor();
}
