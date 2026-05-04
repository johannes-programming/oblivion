const ALARM_NAME = "delete-download-history-older-than-1-hour";
const ONE_HOUR_MS = 60 * 60 * 1000;
const CHECK_EVERY_MINUTES = 5;

async function deleteOldDownloadHistory() {
  const cutoff = new Date(Date.now() - ONE_HOUR_MS).toISOString();

  try {
    const erasedIds = await chrome.downloads.erase({
      startedBefore: cutoff
    });

    console.log(`Removed ${erasedIds.length} old download history entries.`);
  } catch (error) {
    console.error("Failed to remove old download history entries:", error);
  }
}

async function ensureAlarmExists() {
  const existingAlarm = await chrome.alarms.get(ALARM_NAME);

  if (!existingAlarm) {
    await chrome.alarms.create(ALARM_NAME, {
      delayInMinutes: 1,
      periodInMinutes: CHECK_EVERY_MINUTES
    });
  }
}

chrome.runtime.onInstalled.addListener(async () => {
  await deleteOldDownloadHistory();
  await ensureAlarmExists();
});

chrome.runtime.onStartup.addListener(async () => {
  await deleteOldDownloadHistory();
  await ensureAlarmExists();
});

chrome.alarms.onAlarm.addListener(async (alarm) => {
  if (alarm.name === ALARM_NAME) {
    await deleteOldDownloadHistory();
  }
});

ensureAlarmExists();
