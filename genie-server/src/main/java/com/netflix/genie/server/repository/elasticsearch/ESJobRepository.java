/*
 *
 *  Copyright 2015 Netflix, Inc.
 *
 *     Licensed under the Apache License, Version 2.0 (the "License");
 *     you may not use this file except in compliance with the License.
 *     You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0
 *
 *     Unless required by applicable law or agreed to in writing, software
 *     distributed under the License is distributed on an "AS IS" BASIS,
 *     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *     See the License for the specific language governing permissions and
 *     limitations under the License.
 *
 */
package com.netflix.genie.server.repository.elasticsearch;

import com.netflix.genie.common.model.Job;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

/**
 * CRUD repository for Job entities within Elasticsearch.
 *
 * @author tgianos
 */
public interface ESJobRepository extends ElasticsearchRepository<Job, String> {
    /**
     * Find jobs by tags.
     *
     * @param tag The tag to search for
     * @param pageRequest The page of jobs to get
     * @return the jobs that were found
     */
    List<Job> findByTagsContains(final String tag, final PageRequest pageRequest);
}
