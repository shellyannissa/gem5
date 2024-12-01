#include "mem/cache/prefetch/context_based_prefetcher.hh"
#include "debug/HWPrefetch.hh"
#include "params/ContextBasedPrefetcher.hh"
#include <cmath>

namespace gem5
{

namespace prefetch
{

int ContextBasedPrefetcher::globalCounter = 0; // Initialize the global counter

ContextBasedPrefetcher::ContextBasedPrefetcher(const ContextBasedPrefetcherParams &p)
    : Queued(p),
      prefetchWindow(p.prefetch_window),
      rewardFunction(p.target_prefetch_distance, p.prefetch_window)
{
}

void
ContextBasedPrefetcher::calculatePrefetch(const PrefetchInfo &pfi,
                                          std::vector<AddrPriority> &addresses,
                                          const CacheAccessor &cache)
{
    Addr addr = pfi.getAddr();
    int context = pfi.getPC(); // Use PC as context
    int key = hash(context);

    // Increment the global counter for each memory access
    globalCounter++;

    // Data collection
    for (Addr a : previousAccesses) {
        int prev_key = hash(a);
        addToState(prev_key, addr);
    }

    // Prediction
    if (states.find(key) != states.end()) {
        Addr best_addr = getBestAddress(key);
        prefetchQueue.push_back({best_addr, key, (int)prefetchQueue.size()});
    }

    // Feedback
    updateScores(addr);

    // Send prefetch
    sendPrefetch(addresses);

    // Update previous accesses
    previousAccesses.push_back(addr);
    if (previousAccesses.size() > prefetchWindow) {
        previousAccesses.pop_front();
    }
}

void
ContextBasedPrefetcher::notifyFill(const CacheAccessProbeArg &arg)
{
    // Implement if needed
}

int
ContextBasedPrefetcher::hash(int context) const
{
    // Simple hash function
    return context % 1024;
}

void
ContextBasedPrefetcher::addToState(int key, Addr addr)
{
    states[key].ptrs[addr] = 0;
    states[key].counter = globalCounter; // Record the current global counter value
}

Addr
ContextBasedPrefetcher::getBestAddress(int key) const
{
    const auto &ptrs = states.at(key).ptrs;
    if (ptrs.empty()) {
        return 0; // Handle case where there are no addresses
    }
    return std::max_element(ptrs.begin(), ptrs.end(),
                            [](const auto &a, const auto &b) {
                                return a.second < b.second;
                            })->first;
}

void
ContextBasedPrefetcher::updateScores(Addr addr)
{
    for (auto &p : prefetchQueue) {
        if (p.addr == addr) {
            int last_seen = states[p.key].counter; // Get the last seen counter value
            int distance = globalCounter - last_seen; // Calculate the elapsed memory accesses
            int reward = rewardFunction(distance);
            states[p.key].ptrs[addr] += reward;
        }
    }
}

void
ContextBasedPrefetcher::sendPrefetch(std::vector<AddrPriority> &addresses)
{
    if (!prefetchQueue.empty()) {
        Addr next_pref = prefetchQueue.front().addr;
        prefetchQueue.pop_front();
        addresses.push_back(AddrPriority(next_pref, 0));
        DPRINTF(HWPrefetch, "Generated prefetch %#lx\n", next_pref);
    }
}

} // namespace prefetch
} // namespace gem5