#ifndef __MEM_CACHE_PREFETCH_CONTEXT_BASED_PREFETCHER_HH__
#define __MEM_CACHE_PREFETCH_CONTEXT_BASED_PREFETCHER_HH__

#include <unordered_map>
#include <deque>
#include <vector>
#include "mem/cache/prefetch/queued.hh"

namespace gem5
{

struct ContextBasedPrefetcherParams;

namespace prefetch
{

class RewardFunction
{
  public:
    RewardFunction(int target_distance, int window_size)
        : targetDistance(target_distance), windowSize(window_size) {}

    int operator()(int distance) const
    {

        double a = 4.0;    // Height of the peak
        double b = targetDistance;   // Position of the peak
        double c = 10.0;   // Width of the peak

        // Parameters for the exponential tail
        double d = 1;   // Exponential decay factor
        double e = 100.0;   // Decay rate

        // Gaussian-like peak term
        double peak = a * exp(-pow(distance - b, 2) / (2 * c * c));

        // Exponential decay term
        double decay = -d * exp(distance / e);

        // Total reward
        return int((peak + decay) * 100);
    }

  private:
    int targetDistance;
    int windowSize;
};

class ContextBasedPrefetcher : public Queued
{
  public:
    ContextBasedPrefetcher(const ContextBasedPrefetcherParams &p);
    ~ContextBasedPrefetcher() = default;

    void calculatePrefetch(const PrefetchInfo &pfi,
                           std::vector<AddrPriority> &addresses,
                           const CacheAccessor &cache) override;

    void notifyFill(const CacheAccessProbeArg &arg) override;

  private:
    struct State {
        std::unordered_map<Addr, int> ptrs;
        int counter; // Single counter for the context
    };

    struct PrefetchEntry {
        Addr addr;
        int key;
        int index;
    };

    int prefetchWindow;
    RewardFunction rewardFunction;
    std::unordered_map<int, State> states;
    std::deque<Addr> previousAccesses;
    std::deque<PrefetchEntry> prefetchQueue;

    static int globalCounter; // Global counter to track memory accesses

    int hash(int context) const;
    void addToState(int key, Addr addr);
    Addr getBestAddress(int key) const;
    void updateScores(Addr addr);
    void sendPrefetch(std::vector<AddrPriority> &addresses);
};

} // namespace prefetch
} // namespace gem5

#endif // __MEM_CACHE_PREFETCH_CONTEXT_BASED_PREFETCHER_HH__
